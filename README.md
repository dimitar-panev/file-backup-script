# File Backup Utility

A simple Python script that creates timestamped backups of files and directories, and automatically removes old backups after a specified number of days.

## What It Does

- Creates a copy of your file or directory with a timestamp (format: YYYYMMDD_HHMMSS)
- Stores backups in a designated backup directory
- Automatically deletes backups older than a specified number of days (default: 7 days)
- Handles errors gracefully if the source path doesn't exist

## Requirements

No external packages required. Uses only Python standard library:
- Python 3.6+
- Built-in modules: `os`, `shutil`, `pathlib`, `datetime`

## How to Use

1. Edit the script and set these variables:
   - `SOURCE`: The path to the file or directory you want to backup
   - `BACKUP_DIR`: The directory where backups will be stored
   - `KEEP_DAYS`: Number of days to keep backups (default: 7)

2. Run the script:
   ```bash
   python main.py
   ```

## Example

```python
SOURCE = "/Users/username/Documents/my_project"
BACKUP_DIR = "/Users/username/Backups"
KEEP_DAYS = 7

create_backup(SOURCE, BACKUP_DIR, KEEP_DAYS)
```

This will create a backup folder named `backup_20250504_143022` in your backup directory and remove any backups older than 7 days.
