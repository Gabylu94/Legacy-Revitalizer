import datetime
import json
import os
import hashlib


class Authenticator:
    """Handles user authentication securely."""

    def __init__(self):
        self._credentials = {
            "username": os.environ.get("APP_USERNAME", "admin"),
            "password_hash": self._hash_password(
                os.environ.get("APP_PASSWORD", "12345")
            ),
        }

    @staticmethod
    def _hash_password(password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def authenticate(self, username: str, password: str) -> bool:
        password_hash = self._hash_password(password)
        return (
            username == self._credentials["username"]
            and password_hash == self._credentials["password_hash"]
        )


class DataManager:
    """Manages in-memory data items (add, show, list)."""

    def __init__(self):
        self._items: list[dict] = []

    def add_item(self, value: str) -> None:
        if not value or not value.strip():
            print("Error: Value cannot be empty.")
            return
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        item = {
            "id": len(self._items) + 1,
            "value": value,
            "date": timestamp,
        }
        self._items.append(item)
        print(f"Added item #{item['id']}: '{value}'")

    def show_items(self) -> None:
        if not self._items:
            print("No items to display.")
            return
        for item in self._items:
            print(f"Item: {item['id']} - {item['value']} at {item['date']}")

    def get_items(self) -> list[dict]:
        return self._items


class FileHandler:
    """Handles saving data to a file."""

    def __init__(self, filepath: str = "data.json"):
        self._filepath = filepath

    def save(self, items: list[dict]) -> None:
        try:
            with open(self._filepath, "w") as file:
                json.dump(items, file, indent=2)
            print(f"Data saved to '{self._filepath}'.")
        except IOError as e:
            print(f"Error saving file: {e}")


def main():
    authenticator = Authenticator()
    data_manager = DataManager()
    file_handler = FileHandler()

    username = input("User: ")
    password = input("Pass: ")

    if not authenticator.authenticate(username, password):
        print("Authentication failed.")
        return

    print("Welcome!")

    commands = {
        "add": lambda: data_manager.add_item(input("Value: ")),
        "show": lambda: data_manager.show_items(),
        "save": lambda: file_handler.save(data_manager.get_items()),
    }

    while True:
        command = input("What to do? (add/show/save/exit): ").strip().lower()

        if command == "exit":
            print("Goodbye!")
            break

        action = commands.get(command)
        if action:
            action()
        else:
            print(f"Unknown command: '{command}'. Use add/show/save/exit.")


if __name__ == "__main__":
    main()
