from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# Hardcoded secret — intentionally insecure
SECRET_KEY = "my_super_secret_key_123"

DATABASE = "users.db"


def get_db():
    return sqlite3.connect(DATABASE)


@app.route("/")
def home():
    return """
    <h1>Security Audit Demo</h1>
    <p>This application is intentionally vulnerable for security testing.</p>

    <form action="/search" method="GET">
        <input type="text" name="username" placeholder="Search username">
        <button type="submit">Search</button>
    </form>
    """


@app.route("/search")
def search():
    username = request.args.get("username", "")

    db = get_db()

    # INTENTIONALLY VULNERABLE:
    # User input is directly inserted into an SQL query.
    query = "SELECT username FROM users WHERE username = '" + username + "'"

    cursor = db.execute(query)
    results = cursor.fetchall()

    db.close()

    return render_template_string(
        "<h2>Search Results</h2><p>" + str(results) + "</p>"
    )


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    # INTENTIONALLY VULNERABLE:
    # Password is handled without secure hashing.
    if username == "admin" and password == "admin123":
        return "Login successful"

    return "Invalid credentials"


if __name__ == "__main__":
    # INTENTIONALLY INSECURE:
    # Debug mode should not be enabled in production.
    app.run(debug=True)