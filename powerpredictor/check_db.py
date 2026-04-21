import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Get all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Database Tables:")
print("=" * 50)
for table in tables:
    print(f"- {table[0]}")
    # Get table info
    cursor.execute(f"PRAGMA table_info({table[0]});")
    columns = cursor.fetchall()
    print(f"  Columns: {[col[1] for col in columns]}")
    # Count rows
    cursor.execute(f"SELECT COUNT(*) FROM {table[0]};")
    count = cursor.fetchone()[0]
    print(f"  Rows: {count}")
    print()

conn.close()
