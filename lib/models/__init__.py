import sqlite3
import os

# Use absolute path to lib/company.db
db_path = os.path.join(os.path.dirname(__file__), '..', 'company.db')
CONN = sqlite3.connect(db_path)
CURSOR = CONN.cursor()
