# db_search_good.py
import sqlite3

def search_user(username: str):
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (id INTEGER, username TEXT, role TEXT)")
    cursor.execute("INSERT INTO users VALUES (1, 'admin', 'Administrator'), (2, 'guest', 'Guest')")
    
    try:
        # パラメータプレースホルダ（?）を使用し、値をタプルで渡すことで安全に処理
        query = "SELECT role FROM users WHERE username = ?"
        cursor.execute(query, (username,))
        return cursor.fetchall()
    except Exception as e:
        return f"Error: {e}"
    finally:
        conn.close()

if __name__ == "__main__":
    user_in = input("検索するユーザー名を入力してください: ")
    print("検索結果:", search_user(user_in))
