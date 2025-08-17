"""
To-Do List Manager (CLI)
------------------------
Features:
- Add, list, complete, update, delete tasks
- Optional due date
- Persistent storage in JSON
- Search & filter by status
"""

import json
import os
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import List, Optional

DB_FILE = "todos.json"
DATE_FMT = "%Y-%m-%d"


@dataclass
class Todo:
    id: int
    title: str
    done: bool = False
    created_at: str = datetime.now().strftime(DATE_FMT)
    due_date: Optional[str] = None
    notes: Optional[str] = None


class TodoManager:
    def __init__(self, db_path: str = DB_FILE):
        self.db_path = db_path
        self.todos: List[Todo] = []
        self._load()

    def _load(self):
        if not os.path.exists(self.db_path):
            self._save()
        else:
            try:
                with open(self.db_path, "r", encoding="utf-8") as f:
                    raw = json.load(f)
                self.todos = [Todo(**item) for item in raw]
            except Exception:
                self.todos = []
                self._save()

    def _save(self):
        with open(self.db_path, "w", encoding="utf-8") as f:
            json.dump([asdict(t) for t in self.todos], f, indent=2)

    def _next_id(self) -> int:
        return max([t.id for t in self.todos], default=0) + 1

    def add(self, title: str, due_date: Optional[str] = None, notes: Optional[str] = None) -> Todo:
        if due_date:
            # validate date
            try:
                datetime.strptime(due_date, DATE_FMT)
            except ValueError:
                raise ValueError(f"Due date must be {DATE_FMT} (e.g., 2025-08-17)")
        todo = Todo(id=self._next_id(), title=title, due_date=due_date, notes=notes)
        self.todos.append(todo)
        self._save()
        return todo

    def list(self, only_open: bool = False) -> List[Todo]:
        return [t for t in self.todos if (not only_open or not t.done)]

    def get(self, todo_id: int) -> Optional[Todo]:
        return next((t for t in self.todos if t.id == todo_id), None)

    def complete(self, todo_id: int) -> bool:
        t = self.get(todo_id)
        if not t:
            return False
        t.done = True
        self._save()
        return True

    def delete(self, todo_id: int) -> bool:
        before = len(self.todos)
        self.todos = [t for t in self.todos if t.id != todo_id]
        changed = len(self.todos) != before
        if changed:
            self._save()
        return changed

    def update(self, todo_id: int, title: Optional[str] = None,
               due_date: Optional[str] = None, notes: Optional[str] = None) -> bool:
        t = self.get(todo_id)
        if not t:
            return False
        if title:
            t.title = title
        if due_date is not None:
            if due_date != "":
                try:
                    datetime.strptime(due_date, DATE_FMT)
                except ValueError:
                    raise ValueError(f"Due date must be {DATE_FMT}")
                t.due_date = due_date
            else:
                t.due_date = None
        if notes is not None:
            t.notes = notes
        self._save()
        return True

    def search(self, keyword: str) -> List[Todo]:
        k = keyword.lower()
        return [t for t in self.todos if k in t.title.lower() or (t.notes and k in t.notes.lower())]


def print_todos(todos: List[Todo], header: str = "Tasks"):
    print(f"\n=== {header} ({len(todos)}) ===")
    if not todos:
        print("No tasks.")
        return
    for t in todos:
        status = "✅" if t.done else "⏳"
        due = f" | due: {t.due_date}" if t.due_date else ""
        notes = f" | notes: {t.notes}" if t.notes else ""
        print(f"[{t.id}] {status} {t.title} (created: {t.created_at}{due}{notes})")


def menu():
    mgr = TodoManager()
    print("📝 To-Do List Manager")
    while True:
        print("\n--- Menu ---")
        print("1. Add task")
        print("2. List all")
        print("3. List open")
        print("4. Complete task")
        print("5. Update task")
        print("6. Delete task")
        print("7. Search")
        print("8. Exit")
        choice = input("Choose: ").strip()
        try:
            if choice == "1":
                title = input("Title: ").strip()
                due = input(f"Due date ({DATE_FMT}) or blank: ").strip()
                notes = input("Notes (optional): ").strip()
                todo = mgr.add(title, due if due else None, notes if notes else None)
                print(f"✅ Added task #{todo.id}")
            elif choice == "2":
                print_todos(mgr.list(), "All Tasks")
            elif choice == "3":
                print_todos(mgr.list(only_open=True), "Open Tasks")
            elif choice == "4":
                tid = int(input("Task ID to complete: "))
                print("✅ Completed" if mgr.complete(tid) else "❌ Not found")
            elif choice == "5":
                tid = int(input("Task ID to update: "))
                title = input("New title (blank to skip): ").strip()
                due = input(f"New due date ({DATE_FMT}) or blank to clear/skip: ").strip()
                notes = input("New notes (blank to skip, '-' to clear): ").strip()
                notes_val = None if notes == "" else (None if notes == "-" else notes)
                updated = mgr.update(tid, title if title else None, ("" if due == "" else due) if due != "" else "", notes_val)
                print("✅ Updated" if updated else "❌ Not found")
            elif choice == "6":
                tid = int(input("Task ID to delete: "))
                print("🗑️ Deleted" if mgr.delete(tid) else "❌ Not found")
            elif choice == "7":
                kw = input("Keyword: ").strip()
                print_todos(mgr.search(kw), f"Search '{kw}'")
            elif choice == "8":
                print("👋 Bye!")
                break
            else:
                print("❌ Invalid option.")
        except ValueError as e:
            print(f"❌ {e}")


if __name__ == "__main__":
    menu()