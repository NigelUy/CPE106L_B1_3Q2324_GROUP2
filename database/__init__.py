import os.path
from pathlib import Path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

db_name = "db.db"

db_path = os.path.join(BASE_DIR, db_name)
os.getcwd()