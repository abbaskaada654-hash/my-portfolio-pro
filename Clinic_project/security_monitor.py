import sqlite3
from datetime import datetime

# Database Initialization
def init_monitor_db():
    conn = sqlite3.connect('security_logs.db')
    c = conn.cursor()
    # Table to store login attempts, status, and timestamps
    c.execute('''CREATE TABLE IF NOT EXISTS access_logs 
                 (id INTEGER PRIMARY KEY, username TEXT, status TEXT, time TEXT)''')
    conn.commit()
    conn.close()

# Logging Function
def log_attempt(user, status):
    conn = sqlite3.connect('security_logs.db')
    c = conn.cursor()
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO access_logs (username, status, time) VALUES (?, ?, ?)", 
              (user, status, time_now))
    conn.commit()
    
    # Real-time Security Alert Logic
    if status == "FAILED":
        print(f"⚠️ SECURITY ALERT: Suspicious login attempt for user: {user} at {time_now}")
    else:
        print(f"✅ ACCESS GRANTED: Welcome {user}.")
    
    conn.close()

if __name__ == "__main__":
    init_monitor_db()
    print("-" * 50)
    print("      ACTIVE SECURITY MONITORING SYSTEM")
    print("      Developed by: Eng. Abbas Kaddah")
    print("-" * 50)
    
    user_input = input("Enter Username: ")
    pass_input = input("Enter Password: ")
    
    # Secure Authentication Simulation
    if pass_input == "Abbas123":
        log_attempt(user_input, "SUCCESS")
    else:
        log_attempt(user_input, "FAILED")