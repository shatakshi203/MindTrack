#!/usr/bin/env python3

import sqlite3

try:
    conn = sqlite3.connect('backend/mindtrack.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT email, full_name FROM users LIMIT 5')
    users = cursor.fetchall()
    
    print('Test users:')
    for user in users:
        print(f'  {user[0]} - {user[1]}')
    
    conn.close()
    
except Exception as e:
    print(f'Error: {e}')
