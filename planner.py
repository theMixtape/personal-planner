from task import Task

class Planner:
    def __init__(self):
        self.tasks = {}
        self.next_id = 1

    def add_task(self, title, date, desc):
        task = Task(self.next_id, title, date, desc)
        self.tasks[task.task_id] = task
        self.next_id += 1
        return task

    def get_task(self, task_id):
        if task_id not in self.tasks:
            print(f"[!] Не існує завдання з номером {task_id}")
            return None
        return self.tasks[task_id]

    def remove_task(self, task_id):
        task = self.get_task(task_id)
        if task:
            del self.tasks[task_id]
        return task

    def mark_task_completed(self, task_id):
        task = self.get_task(task_id)
        if task:
            task.mark_completed()
        return task

    def search_by_title(self, title):
        search_title = title.casefold()
        return [
            task for task in self.all_tasks()
            if search_title in task.title.casefold()
        ]

    def all_tasks(self):
        return sorted(self.tasks.values(), key=lambda task: task.task_id)

    def dict(self):
        return {
            "next_id": self.next_id,
            "tasks": [t.dict() for t in self.all_tasks()],
        }

    @classmethod
    def from_dict(cls, data):
        planner = cls()
        planner.next_id = data.get("next_id", 1)
        for task_data in data.get("tasks", []):
            task = Task.from_dict(task_data)
            planner.tasks[task.task_id] = task
            if task.task_id >= planner.next_id:
                planner.next_id = task.task_id + 1
        return planner

