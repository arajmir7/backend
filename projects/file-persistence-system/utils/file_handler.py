import json
import os
from datetime import datetime


class FileHandler:
    def __init__(self, filepath):
        self.filepath = filepath
        self.backup_path = filepath + ".backup"

    def load_data(self):
        """Load data safely from JSON file"""
        try:
            with open(self.filepath, "r") as f:
                return json.load(f)

        except FileNotFoundError:
            print("⚠ Data file not found. Creating new dataset.")
            return []

        except json.JSONDecodeError:
            print("⚠ Corrupted JSON detected. Restoring backup.")
            return self.restore_backup()

    def save_data(self, data):
        """Save data with backup protection"""
        try:
            if os.path.exists(self.filepath):
                os.replace(self.filepath, self.backup_path)

            with open(self.filepath, "w") as f:
                json.dump(data, f, indent=2)

            return True

        except Exception as e:
            print("❌ Write failed:", e)
            self.restore_backup()
            return False

    def restore_backup(self):
        """Restore data from backup"""
        if os.path.exists(self.backup_path):
            with open(self.backup_path, "r") as f:
                return json.load(f)

        print("❌ No backup found.")
        return []
    
    
