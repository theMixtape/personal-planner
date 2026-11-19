import sys

from menu import Menu
from storage import Storage


def main():
    storage = Storage("planner.json")
    planner = storage.load()
    Menu(planner, storage).start()


if __name__ == "__main__":
    main()