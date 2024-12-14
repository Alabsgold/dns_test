from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

# Function to get all blocked domains
def get_blocked_domains():
    conn = sqlite3.connect("blocklist.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, domain FROM blocklist")
    domains = cursor.fetchall()
    conn.close()
    return domains

# Function to add a domain to the blocklist
def add_blocked_domain(domain):
    conn = sqlite3.connect("blocklist.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO blocklist (domain) VALUES (?)", (domain,))
        conn.commit()
    except sqlite3.IntegrityError:
        pass  # Ignore duplicates
    conn.close()

# Function to remove a domain from the blocklist
def remove_blocked_domain(domain_id):
    conn = sqlite3.connect("blocklist.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM blocklist WHERE id = ?", (domain_id,))
    conn.commit()
    conn.close()

# Route to display the blocklist
@app.route("/")
def index():
    domains = get_blocked_domains()
    return render_template("index.html", domains=domains)

# Route to add a domain
@app.route("/add", methods=["POST"])
def add():
    domain = request.form.get("domain")
    if domain:
        add_blocked_domain(domain)
    return redirect("/")

# Route to remove a domain
@app.route("/remove/<int:domain_id>")
def remove(domain_id):
    remove_blocked_domain(domain_id)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Default to port 5000 if PORT is not set
    app.run(host="0.0.0.0", port=port)