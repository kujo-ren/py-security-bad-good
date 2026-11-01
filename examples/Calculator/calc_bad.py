#clac_bad.py

def calculate(user_input: str):
    try:
        return eval(user_input)
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    user_in = input("数式を入力してください: ")
    print("結果:", calculate(user_in))
