# calc_good.py

import ast

def calculate(user_input: str):
    try:
        # 文字列を安全に数値（または単純な四則演算の構造）として評価する
        return ast.literal_eval(user_input)
    except Exception:
        return "Error: 不正または安全ではない入力です"

if __name__ == "__main__":
    user_in = input("数式を入力してください: ")
    print("結果:", calculate(user_in))
