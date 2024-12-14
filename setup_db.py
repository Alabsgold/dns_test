import sqlite3

# Create and connect to the database
conn = sqlite3.connect("blocklist.db")
cursor = conn.cursor()

# Create the table for blocked domains
cursor.execute("""
CREATE TABLE IF NOT EXISTS blocklist (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    domain TEXT UNIQUE NOT NULL
)
""")

# Add some initial blocked domains
blocked_domains = ["example.com", "badwebsite.com"]
for domain in blocked_domains:
    try:
        cursor.execute("INSERT INTO blocklist (domain) VALUES (?)", (domain,))
    except sqlite3.IntegrityError:
        pass  # Ignore duplicates

# Commit and close
conn.commit()
conn.close()

print("Database setup complete.")
