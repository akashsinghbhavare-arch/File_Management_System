# File Management System

A simple, menu-driven command-line program for managing files in the current
working directory. It is written in Python and uses only the standard library.

## Features

- Create an empty file
- Append text to an existing file
- Display a file's contents
- Rename a file
- Delete a file after confirmation
- List files in the current directory

## Requirements

- Python 3

No third-party packages are required.

## Run

Open a terminal in the project directory and run:

```bash
python filemanagement.py
```

On Windows, you can also use:

```powershell
py filemanagement.py
```

## Usage

Choose an option from the menu:

| Option | Action |
| --- | --- |
| 1 | Create a file |
| 2 | Append text to a file |
| 3 | Read a file |
| 4 | Rename a file |
| 5 | Delete a file |
| 6 | List files in the current directory |
| 7 | Exit |

File names are resolved relative to the directory from which the program is
run. Deleting a file requires typing `yes` at the confirmation prompt.
