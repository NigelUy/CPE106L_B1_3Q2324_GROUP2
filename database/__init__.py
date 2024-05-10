import os 
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

db_name = "datebase.db"

db_path = os.path.join(BASE_DIR, db_name)
print("base dir path", BASE_DIR)