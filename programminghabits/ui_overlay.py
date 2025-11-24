import os
import random
import subprocess
import dbus
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFrame, QGraphicsDropShadowEffect
from PyQt6.QtCore import Qt, QTimer, QUrl
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtMultimedia import QSoundEffect
from programminghabits.utils import resource_path

class BreakOverlay(QWidget):
    def __init__(self, duration_seconds, tips, on_finish_callback):
        super().__init__()
        self.duration_left = duration_seconds
        self.on_finish = on_finish_callback

        self.sound_path = resource_path("assets/alert.wav")

        self.pause_media()
        self.play_sound()

        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.FramelessWindowHint | Qt.WindowType.Tool)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.showFullScreen()

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(main_layout)

        self.card = QFrame()
        self.card.setStyleSheet("QFrame { background-color: #222222; border-radius: 24px; }")
        self.card.setFixedSize(600, 400)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(50)
        shadow.setColor(QColor(0, 0, 0, 150))
        shadow.setOffset(0, 10)
        self.card.setGraphicsEffect(shadow)

        card_layout = QVBoxLayout()
        card_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        card_layout.setSpacing(20)
        self.card.setLayout(card_layout)

        accent_color = self.get_system_accent_color()

        tip_text = random.choice(tips) if tips else "Take a deep breath and smile..."
        self.tip_label = QLabel(tip_text)
        self.tip_label.setStyleSheet("color: #EEEEEE; font-size: 24px; font-weight: 500; padding: 10px;")
        self.tip_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tip_label.setWordWrap(True)
        card_layout.addWidget(self.tip_label)

        self.timer_label = QLabel(self.format_time(self.duration_left))
        self.timer_label.setStyleSheet(f"color: {accent_color}; font-size: 72px; font-weight: bold;")
        self.timer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        card_layout.addWidget(self.timer_label)

        self.skip_btn = QPushButton("Skip Break")
        self.skip_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.skip_btn.setStyleSheet("""
            QPushButton { background-color: #444444; color: white; font-size: 14px;
                          padding: 8px 16px; border-radius: 8px; border: none; }
            QPushButton:hover { background-color: #666666; }
        """)
        self.skip_btn.clicked.connect(self.close_overlay)
        card_layout.addWidget(self.skip_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        main_layout.addWidget(self.card)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.tick)
        self.timer.start(1000)

    def get_system_accent_color(self):
        """
        Queries GNOME settings to find the exact accent color.
        Trying multiple approaches
        Returns a Hex string.
        """
        try:
            # Try modern GNOME accent-color (Ubuntu 22.04+)
            output = subprocess.check_output(
                ["gsettings", "get", "org.gnome.desktop.interface", "accent-color"],
                stderr=subprocess.DEVNULL
            ).decode("utf-8").strip().strip("'")

            colors = {
                'green': '#26a269',   # Ubuntu Yaru Green
                'orange': '#e95420',  # Ubuntu Classic
                'blue': '#3584e4',    # Adwaita
                'teal': '#21a6cb',
                'purple': '#9141ac',
                'red': '#e01b24',
                'yellow': '#f5c211',
                'bark': '#787c72',
                'pink': '#d56199',
                'slate': '#5e5c64'
            }
            if output in colors:
                return colors[output]

        except Exception:
            pass

        # Fallback: Try to guess based on GTK Theme Name
        try:
            theme = subprocess.check_output(
                ["gsettings", "get", "org.gnome.desktop.interface", "gtk-theme"],
                stderr=subprocess.DEVNULL
            ).decode("utf-8").strip().strip("'")

            if "Yaru" in theme and "dark" not in theme and "blue" not in theme:
                return "#e95420" # Standard Yaru is often Orange
            if "Mint" in theme:
                return "#92b752" # Mint Green
        except Exception:
            pass

        # Qt Highlight (System Theme Plugin)
        qt_color = self.palette().color(QPalette.ColorRole.Highlight).name()
        if qt_color not in ["#000000", "#ffffff"]:
            return qt_color

        # Ultimate Fallback (Teal)
        return "#88C0D0"

    def pause_media(self):
        try:
            bus = dbus.SessionBus()
            for service in bus.list_names():
                if service.startswith('org.mpris.MediaPlayer2.'):
                    try:
                        player = dbus.SessionBus().get_object(service, '/org/mpris/MediaPlayer2')
                        interface = dbus.Interface(player, dbus_interface='org.mpris.MediaPlayer2.Player')
                        interface.Pause()
                    except: pass
        except: pass

    def play_sound(self):
        self.effect = QSoundEffect()
        self.effect.setSource(QUrl.fromLocalFile(self.sound_path))
        self.effect.setVolume(0.5)
        self.effect.play()
        # Above method can fail
        try: subprocess.Popen(["paplay", self.sound_path], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        except: pass

    def format_time(self, s): return f"{divmod(s, 60)[0]:02d}:{divmod(s, 60)[1]:02d}"

    def tick(self):
        self.duration_left -= 1
        self.timer_label.setText(self.format_time(self.duration_left))
        if self.duration_left <= 0: self.close_overlay()

    def close_overlay(self):
        self.timer.stop()
        self.close()
        self.on_finish()
