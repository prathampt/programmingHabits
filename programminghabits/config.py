import json
import os

CONFIG_DIR = os.path.expanduser("~/.config/programminghabits")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")

DEFAULT_CONFIG = {
    "enabled": True,
    "focus_duration": 25,
    "break_duration": 5,
    "tips": [
        "Hydrate. Your brain is 73% water.",
        "20-20-20 Rule: Look at something 20 feet away for 20 seconds.",
        "Your spine supports your logic. Give it a stretch.",
        "Close your eyes, breathe deeply and smile...",
        "Get up and walk around the room."
    ]
}

class ConfigManager:
    def __init__(self):
        self.ensure_config_exists()
        self.data = self.load_config()

    def ensure_config_exists(self):
        if not os.path.exists(CONFIG_DIR):
            os.makedirs(CONFIG_DIR)
        if not os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'w') as f:
                json.dump(DEFAULT_CONFIG, f, indent=4)

    def load_config(self):
        try:
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)
        except Exception:
            return DEFAULT_CONFIG

    def save_config(self, enabled, focus_min, break_min, tips_list):
        self.data['enabled'] = enabled
        self.data['focus_duration'] = focus_min
        self.data['break_duration'] = break_min
        self.data['tips'] = [t for t in tips_list if t.strip()]
        with open(CONFIG_FILE, 'w') as f:
            json.dump(self.data, f, indent=4)

    def get_enabled(self): return self.data.get('enabled', True)
    def get_focus_seconds(self): return self.data.get('focus_duration', 25) * 60
    def get_break_seconds(self): return self.data.get('break_duration', 5) * 60
    def get_tips(self): return self.data.get('tips', [])
