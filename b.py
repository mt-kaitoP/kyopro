def detect_replacement(N, A):
    # 書き換えが発生したかを判定するフラグ
    replacement = False
    # 書き換えられた整数とその対応する整数の辞書
    replacements = {}

    # 判定処理
    for i in range(N):
        if A[i] != i + 1:
            replacement = True
            replacements[A[i]] = i + 1

    return replacement, replacements

# 入力を受け取る
N = int(input())
A = list(map(int, input().split()))

# 書き換えが発生しているかどうかを判定
replacement, replacements = detect_replacement(N, A)

# 書き換えが発生していない場合
if not replacement:
    print("Correct")

# 書き換えが発生している場合
else:
    for replaced, original in replacements.items():
        print(original, replaced)
