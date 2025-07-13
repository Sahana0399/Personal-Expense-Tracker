import sqlite3

def connect():
    
    conn = sqlite3.connect("expenses_tracker.db")
    cursor = conn.cursor()
    
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS users(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       username TEXT UNIQUE,
                       password TEXT
                    )
                   
     ''')
    conn.commit()
    conn.close()
    
def insert_user(username, password):
   try:
      conn = sqlite3.connect('expenses_tracker.db')
      cursor = conn.cursor()

      # Insert user data
      cursor.execute('''
      INSERT INTO users (username, password)
      VALUES (?, ?)
      ''', (username, password))

      conn.commit()  # Save the changes
      return True
   except sqlite3.IntegrityError:
       return False
   finally:
       conn.close()
       

    
def insert_expense(username, date, category, amount, location):
    conn = sqlite3.connect("expenses_tracker.db")
    cursor = conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS expense (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       username TEXT,
                       date TEXT,
                       category TEXT,
                       amount REAL,
                       location TEXT
                   )
                   ''')
    cursor.execute('''
    INSERT INTO expense(username, date, category, amount, location)               
    VALUES (?,?,?,?,?)
    ''', (username,date,category,amount,location))
    conn.commit()
    conn.close()

def fetch_user(username,password):
    conn = sqlite3.connect("expenses_tracker.db")
    cursor = conn.cursor()
    
    cursor.execute('''
                   SELECT * FROM users WHERE username = ? AND password = ?
                   ''',( username, password))
    
    user = cursor.fetchone()
    conn.close()
    return user
    
    
def fetch_expense(username):
    conn = sqlite3.connect("expenses_tracker.db")
    cursor = conn.cursor()
    
    cursor.execute('''
                   SELECT date, category,amount, location
                   FROM expense
                   WHERE username = ?
                   ORDER BY date DESC
                   ''',( username,))
    
    expenses = cursor.fetchall()
    conn.close()
    return expenses

