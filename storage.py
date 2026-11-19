import json
import os

from planner import Planner


class Storage:
    def __init__(self, filename="planner.json"):
        self.filename = filename

    def save(self, planner):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(planner.dict(), f, ensure_ascii=False, indent=2)

    def load(self):
        if not os.path.exists(self.filename):
            return Planner()
        with open(self.filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        return Planner.from_dict(data)