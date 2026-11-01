import sqlite3

def search_user(username: str):
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (id INTEGER, username TEXT, role TEXT)")
    cursor.execute("INSERT INTO users VALUES (1, 'admin', 'Administrator'), (2, 'guest', 'Guest')")
    
    try:
        query = f"SELECT role FROM users WHERE username = '{username}'"
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        return f"Error: {e}"
    finally:
        conn.close()

if __name__ == "__main__":
    user_in = input("検索するユーザー名を入力してください: ")
    print("検索結果:", search_user(user_in))
