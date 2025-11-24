from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QLabel, QSpinBox,
                             QDialogButtonBox, QCheckBox, QTextEdit, QTabWidget, QWidget)

class SettingsDialog(QDialog):
    def __init__(self, is_enabled, current_work, current_break, current_tips):
        super().__init__()
        self.setWindowTitle("Settings")
        self.resize(400, 350)

        layout = QVBoxLayout()
        self.enable_chk = QCheckBox("Enable Programming Habits")
        self.enable_chk.setChecked(is_enabled)
        layout.addWidget(self.enable_chk)

        tabs = QTabWidget()

        # Timer Tab
        tab_timer = QWidget()
        timer_layout = QVBoxLayout()
        timer_layout.addWidget(QLabel("Focus Duration (minutes):"))
        self.work_spin = QSpinBox()
        self.work_spin.setRange(1, 120)
        self.work_spin.setValue(current_work)
        timer_layout.addWidget(self.work_spin)

        timer_layout.addWidget(QLabel("Break Duration (minutes):"))
        self.break_spin = QSpinBox()
        self.break_spin.setRange(1, 60)
        self.break_spin.setValue(current_break)
        timer_layout.addWidget(self.break_spin)
        timer_layout.addStretch()
        tab_timer.setLayout(timer_layout)
        tabs.addTab(tab_timer, "Timer")

        # Quotes Tab
        tab_quotes = QWidget()
        quotes_layout = QVBoxLayout()
        quotes_layout.addWidget(QLabel("Custom Quotes (One per line):"))
        self.quotes_edit = QTextEdit()
        self.quotes_edit.setPlainText("\n".join(current_tips))
        quotes_layout.addWidget(self.quotes_edit)
        tab_quotes.setLayout(quotes_layout)
        tabs.addTab(tab_quotes, "Quotes")
        layout.addWidget(tabs)

        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)
        self.setLayout(layout)

    def get_values(self):
        return (self.enable_chk.isChecked(), self.work_spin.value(),
                self.break_spin.value(), self.quotes_edit.toPlainText().split('\n'))
