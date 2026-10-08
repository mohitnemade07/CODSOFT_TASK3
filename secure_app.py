from flask import Flask, request, render_template_string
import sqlite3
import os
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Secure: load secret from environment variable
app.config["SECRET_KEY"] = os.environ.get(
    "SECRET_KEY",
    "development-only-key"
)

DATABASE = "users.db"


def get_db():
    return sqlite3.connect(DATABASE)


@app.route("/")
def home():
    return """
    <h1>Secure Security Audit Demo</h1>

    <form action="/search" method="GET">
        <input
            type="text"
            name="username"
            maxlength="50"
            placeholder="Search username"
            required
        >
        <button type="submit">Search</button>
    </form>
    """


@app.route("/search")
def search():
    username = request.args.get("username", "").strip()

    # Basic input validation
    if not username or len(username) > 50:
        return "Invalid username", 400

    db = get_db()

    # Secure: parameterized SQL query
    query = "SELECT username FROM users WHERE username = ?"
    cursor = db.execute(query, (username,))
    results = cursor.fetchall()

    db.close()

    # Data is inserted through a template variable
    return render_template_string(
        """
        <h2>Search Results</h2>
        <p>{{ results }}</p>
        """,
        results=results
    )


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")

    # Example: password should be stored as a hash,
    # not as plaintext in the source code.
    stored_password_hash = os.environ.get("ADMIN_PASSWORD_HASH")

    if not stored_password_hash:
        return "Authentication configuration is missing", 500

    if username == "admin" and check_password_hash(
        stored_password_hash,
        password
    ):
        return "Login successful"

    return "Invalid credentials", 401


if __name__ == "__main__":
    # Secure: debug mode disabled
    app.run(debug=False)