from itertools import permutations

# 일단 입력값을 다 받아준다.
n = int(input())
a = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
ans = []

# 일단 사칙 연산 가능한 경우 전부다 순열 전개
for s in set(permutations('+' * add + '-' * sub + '*' * mul + '/' * div)):
    r = a[0]
    # 딕셔너리를 통해 연산자에 맞는 계산을 실행하도록 한다.
    for i in range(1, n):
        r = {'+': r + a[i], '-': r - a[i], '*': r * a[i], '/': int(r / a[i])}[s[i - 1]]
    ans.append(r)

print(max(ans), min(ans))