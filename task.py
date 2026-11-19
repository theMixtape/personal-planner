class Task:
    def __init__(self, task_id, title, date, desc, completed=False):
        self.task_id = task_id
        self.title = title
        self.date = date
        self.desc = desc
        self.completed = completed

    def dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "date": self.date,
            "desc": self.desc,
            "completed": self.completed
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["task_id"],
            data["title"],
            data["date"],
            data["desc"],
            data.get("completed", False)
        )

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "[Виконано]" if self.completed else "[Активне]"
        return (
            f"╭─ Завдання #{self.task_id} ──────────────────────────\n"
            f"│ {status}  {self.title}\n"
            f"│ Дата: {self.date}\n"
            f"│ Опис: {self.desc}\n"
            f"╰──────────────────────────────────────────────────"
        )
        