import os
import shutil
from pathlib import Path
from datetime import datetime, timedelta

def create_backup(source_dir, backup_base_dir, keep_days=7):
    """
    Copy source directory to timestamped backup folder and delete old backups.
    
    Args:
        source_dir: Path to directory/file to backup
        backup_base_dir: Base directory where backups are stored
        keep_days: Number of days to keep backups (default: 7)
    """
    source_path = Path(source_dir)
    backup_base_path = Path(backup_base_dir)
    
    if not source_path.exists():
        print(f"Error: Source path does not exist: {source_dir}")
        return
    
    # Create backup base directory if it doesn't exist
    backup_base_path.mkdir(parents=True, exist_ok=True)
    
    # Create timestamped backup folder
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = backup_base_path / f"backup_{timestamp}"
    
    # Copy files/folders
    if source_path.is_file():
        backup_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_path, backup_path)
        print(f"Copied file: {source_path} → {backup_path}")
    else:
        shutil.copytree(source_path, backup_path)
        print(f"Copied directory: {source_path} → {backup_path}")
    
    # Delete old backups
    cutoff_time = datetime.now() - timedelta(days=keep_days)
    
    for backup_folder in sorted(backup_base_path.glob("backup_*")):
        if backup_folder.is_dir():
            folder_time = datetime.strptime(backup_folder.name, "backup_%Y%m%d_%H%M%S")
            
            if folder_time < cutoff_time:
                shutil.rmtree(backup_folder)
                print(f"Deleted old backup: {backup_folder}")

if __name__ == "__main__":
    # Example usage
    SOURCE = ""  # Change this
    BACKUP_DIR = ""  # Change this
    KEEP_DAYS = 7 # if you want you can change how many days the backup is kept
    
    create_backup(SOURCE, BACKUP_DIR, KEEP_DAYS)