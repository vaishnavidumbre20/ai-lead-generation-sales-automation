"""
Migrate existing SQLite leads to PostgreSQL.
Set SQLITE_DB_PATH and DATABASE_URL in your .env file.
Run:
    pip install psycopg2-binary python-dotenv
    python migrate_sqlite_to_postgres.py
"""
import sqlite3
import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values

load_dotenv()

# Path to your sqlite DB (from .env)
SQLITE_DB_PATH = os.getenv("SQLITE_DB_PATH", "leads-op-main/leads.db")
DATABASE_URL = os.getenv("DATABASE_URL")

if not os.path.exists(SQLITE_DB_PATH):
    raise SystemExit(f"SQLite DB not found at {SQLITE_DB_PATH}")

if not DATABASE_URL:
    raise SystemExit("DATABASE_URL not set in .env")

print(f"Connecting to SQLite at {SQLITE_DB_PATH}")
src = sqlite3.connect(SQLITE_DB_PATH)
cur = src.cursor()

# Detect columns in old DB
cur.execute("PRAGMA table_info(leads);")
cols = [row[1] for row in cur.fetchall()]
print(f"Detected SQLite 'leads' columns: {cols}")

# Columns we know how to migrate
possible_cols = ["name", "email", "phone", "message", "score", "classification", "created_at"]
select_cols = [c for c in possible_cols if c in cols]

if not select_cols:
     raise SystemExit("No recognizable columns (name, email, etc.) in sqlite leads table.")

sel_sql = "SELECT " + ", ".join(select_cols) + " FROM leads"
cur.execute(sel_sql)
rows = cur.fetchall()
print(f"Found {len(rows)} rows to migrate from SQLite.")

if not rows:
    print("No rows to migrate. Exiting.")
    src.close()
    exit()

print("Connecting to PostgreSQL...")
dst = psycopg2.connect(DATABASE_URL)
dst_cur = dst.cursor()

# Build insert statement for Postgres
# We add 'source' column manually
pg_cols = select_cols + ["source"]
insert_stmt = f"""
INSERT INTO leads ({", ".join(pg_cols)})
VALUES %s
ON CONFLICT DO NOTHING
"""

records = []
for r in rows:
    # Append 'migrated' as the source
    records.append(list(r) + ["migrated"])

print(f"Inserting {len(records)} records into PostgreSQL...")
execute_values(dst_cur, insert_stmt, records, template=None, page_size=100)
dst.commit()
print("Migration committed.")

dst_cur.close()
dst.close()
src.close()
print("All connections closed. Migration complete.")
