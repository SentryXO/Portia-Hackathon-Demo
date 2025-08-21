import sqlite3

def authenticate_user(username, password):
    # SECURITY BUG: SQL Injection vulnerability
    conn = sqlite3.connect('users.db')
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor = conn.execute(query)
    return cursor.fetchone()

def get_user_profile(user_id):
    # SECURITY BUG: No input validation
    conn = sqlite3.connect('users.db')
    query = f"SELECT * FROM profiles WHERE id={user_id}"
    return conn.execute(query).fetchall()