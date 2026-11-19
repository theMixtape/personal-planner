class Menu:
    TEXT = """
    ╭────────────────────────────────╮
    │    Персональний планувальник   │
    ╰────────────────────────────────╯
     ────────────────────────────────
      [1] ➜  Додати завдання
      [2] ➜  Переглянути всі завдання
      [3] ➜  Видалити завдання
      [4] ➜  Позначити завдання виконаним
      [5] ➜  Пошук за назвою
      [0] ➜  Вийти
     ────────────────────────────────
"""

    def __init__(self, library, storage):
        self.library = library
        self.storage = storage
        self.actions = {
            "1": self.add_task,
            "2": self.show_task,
            "3": self.remove_task,
            "4": self.mark_task_completed,
            "5": self.search_tasks,
        }

    def start(self):
        while True:
            print(self.TEXT)
            choice = input("Оберіть дію: ").strip()
            if choice == "0":
                self.storage.save(self.library)
                print("[!] Дані збережено.")
                return
            action = self.actions.get(choice)
            if action is None:
                print("[!] Невірний вибір.")
                continue
            action()

    def add_task(self):
        title = input("Введіть назву ➜  ").strip()
        date = input("Введіть дату ➜  ").strip()
        desc = input("Введіть опис ➜  ").strip()
        if not title or not desc or not date or not date.isdigit():
            print("[!] Помилка: заповніть усі поля правильно (дата має бути числом).")
            return
        task = self.library.add_task(title, date, desc)
        self.storage.save(self.library)
        print(f"[!] Додано завдання: {task}")

    def ask_id(self):
        ask = input("Введіть ID завдання ➜ ").strip()
        if not ask.isdigit():
            print("[!] Помилка: ID завдання має бути числом")
            return
        return int(ask)

    def remove_task(self):
        task_id = self.ask_id()
        if task_id is None:
            return

        removed = self.library.remove_task(task_id)
        if removed:
            self.storage.save(self.library)
            print(f"[!] Завдання видалено: {removed}")

    def mark_task_completed(self):
        task_id = self.ask_id()
        if task_id is None:
            return

        task = self.library.mark_task_completed(task_id)
        if task:
            self.storage.save(self.library)
            print(f"[!] Завдання виконано: {task}")

    def search_tasks(self):
        title = input("Введіть назву для пошуку ➜ ").strip()
        if not title:
            print("[!] Помилка: назва для пошуку не може бути порожньою.")
            return

        tasks = self.library.search_by_title(title)
        if not tasks:
            print("[!] Завдань за такою назвою не знайдено.")
            return

        print(f"[!] Знайдено завдань: {len(tasks)}")
        for task in tasks:
            print(task)
            print()

    def show_task(self):
        tasks = self.library.all_tasks()
        if not tasks:
            print("[!] Бібліотека порожня")
            return
        print(f"[!] Усього завдань: {len(tasks)}")
        for task in tasks:
            print(task)
            print()

        