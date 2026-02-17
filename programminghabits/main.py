import sys
import os

from dbus.mainloop.glib import DBusGMainLoop
from PyQt6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtCore import QTimer

from programminghabits.config import ConfigManager
from programminghabits.ui_overlay import BreakOverlay
from programminghabits.ui_settings import SettingsDialog
from programminghabits.utils import resource_path

ICON_PATH = resource_path("assets/programminghabits.png")

ADD_DEV_MENU = False

class AppController:
    def __init__(self):
        try:
            DBusGMainLoop(set_as_default=True)
        except:
            pass

        self.app = QApplication(sys.argv)
        self.app.setQuitOnLastWindowClosed(False)
        self.cfg = ConfigManager()
        self.state = "FOCUS"
        self.time_left = self.cfg.get_focus_seconds()
        self.overlay_window = None

        self.setup_tray()
        self.timer = QTimer()
        self.timer.timeout.connect(self.tick)
        self.timer.start(1000)
        self.open_settings()

    def setup_tray(self):
        self.tray = QSystemTrayIcon()
        if os.path.exists(ICON_PATH): self.tray.setIcon(QIcon(ICON_PATH))
        else: self.tray.setIcon(self.app.style().standardIcon(self.app.style().StandardPixmap.SP_ComputerIcon))
        self.tray.setVisible(True)

        self.menu = QMenu()
        self.status_action = QAction("Ready"); self.status_action.setEnabled(False)
        self.menu.addAction(self.status_action)
        self.menu.addSeparator()

        settings = QAction("Settings", self.menu)
        settings.triggered.connect(self.open_settings)
        self.menu.addAction(settings)

        dev_menu = QMenu("Developer Tools", self.menu)
        test_bk = QAction("Test Break (5s)", self.menu)
        test_bk.triggered.connect(self.force_break)
        dev_menu.addAction(test_bk)
        if (ADD_DEV_MENU):
            self.menu.addMenu(dev_menu)

        self.menu.addSeparator()
        rst = QAction("Reset Timer", self.menu); rst.triggered.connect(self.reset_cycle)
        self.menu.addAction(rst)
        quit_app = QAction("Quit", self.menu); quit_app.triggered.connect(self.app.quit)
        self.menu.addAction(quit_app)
        self.tray.setContextMenu(self.menu)

    def force_break(self):
        self.state="BREAK"; self.timer.stop()
        self.overlay_window = BreakOverlay(5, self.cfg.get_tips(), self.end_break)

    def tick(self):
        if not self.cfg.get_enabled():
            self.tray.setToolTip("Disabled"); self.status_action.setText("Status: Disabled")
            return
        if self.state == "FOCUS":
            self.time_left -= 1
            self.update_ui()
            if self.time_left <= 0: self.start_break()

    def update_ui(self):
        m, s = divmod(self.time_left, 60)
        self.tray.setToolTip(f"{m:02d}:{s:02d} - Working")
        self.status_action.setText(f"{m:02d}:{s:02d} - Working")

    def start_break(self):
        self.state = "BREAK"; self.timer.stop()
        self.overlay_window = BreakOverlay(self.cfg.get_break_seconds(), self.cfg.get_tips(), self.end_break)

    def end_break(self):
        self.state = "FOCUS"; self.time_left = self.cfg.get_focus_seconds(); self.timer.start(1000)
        self.tray.showMessage("Back to Work", "Focus mode on.", QSystemTrayIcon.MessageIcon.Information, 2000)

    def reset_cycle(self):
        if self.overlay_window: self.overlay_window.close()
        self.end_break()

    def open_settings(self):
        dlg = SettingsDialog(self.cfg.get_enabled(), int(self.cfg.get_focus_seconds()/60),
                             int(self.cfg.get_break_seconds()/60), self.cfg.get_tips())
        dlg.activateWindow(); dlg.raise_()
        if dlg.exec():
            e, w, b, t = dlg.get_values()
            self.cfg.save_config(e, w, b, t); self.reset_cycle()

    def run_logic(self):
        sys.exit(self.app.exec())

def main():
    controller = AppController()
    controller.run_logic()

if __name__ == "__main__":
    main()
