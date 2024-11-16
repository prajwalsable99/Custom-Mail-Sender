import sqlite3
import pandas as pd

def init_db(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        email TEXT UNIQUE
    )
    """)

   
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS email_logs (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        recipient_email TEXT,
        content TEXT,
        status TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    conn.commit()
    conn.close()

def insert_user(db_name, email):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Insert user if not exists
    cursor.execute("INSERT OR IGNORE INTO users (email) VALUES (?)", (email,))
    conn.commit()

    # Fetch the user's ID
    cursor.execute("SELECT id FROM users WHERE email = ?", (email,))
    user_id = cursor.fetchone()[0]
    conn.close()
    return user_id

def insert_email_log(db_name, user_id, recipient_email, content, status):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO email_logs (user_id, recipient_email, content, status) 
    VALUES (?, ?, ?, ?)
    """, (user_id, recipient_email, content, status))
    conn.commit()
    conn.close()

def fetch_email_logs_by_user(db_name, user_id):
    conn = sqlite3.connect(db_name)
    df = pd.read_sql_query("""
    SELECT  recipient_email, content,timestamp, status FROM email_logs WHERE user_id = ?
    """, conn, params=(user_id,))
    conn.close()
    return df
