# Spaghetti Code Refactor - Python

## Description

This project takes an intentionally messy Python script (`process_data.py`) and refactors it into clean, maintainable code following SOLID principles and Python best practices.

The application is a simple CLI tool that authenticates a user and allows them to add, view, and save data items.

## How to Run

```bash
python process_data.py
```

Default credentials: `admin` / `12345`

You can override credentials via environment variables:

```bash
export APP_USERNAME="myuser"
export APP_PASSWORD="mypassword"
python process_data.py
```

## What Was Refactored

| Problem | Solution |
|---|---|
| Global variables (`l`, `d`) | Encapsulated in classes with instance attributes |
| Cryptic names (`fn`, `a`, `b`, `l`, `d`) | Descriptive names (`add_item`, `value`, `data_manager`) |
| One function doing everything (`fn`) | Separated into `DataManager`, `FileHandler`, `Authenticator` classes |
| No error handling | Added input validation and try-except for file I/O |
| Hardcoded credentials in plain text | Passwords hashed with SHA-256; configurable via environment variables |
| `open()` without context manager | Uses `with` statement for safe file handling |
| Saving data as raw `str(list)` | Uses `json.dump()` for proper serialization |
| Dead code (`calculate_something_else`) | Removed entirely |
| No entry point guard | Added `if __name__ == "__main__"` |
| No input sanitization | Added `.strip().lower()` on commands, empty value check |

## Principles Applied

- **Single Responsibility**: Each class has one job (auth, data, file I/O)
- **Open/Closed**: New commands can be added to the `commands` dict without modifying existing logic
- **Dependency Inversion**: `main()` composes objects; classes don't depend on each other
- **DRY**: No repeated logic
- **Clean Code**: Descriptive naming, f-strings, type hints
