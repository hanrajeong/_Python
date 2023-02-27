# 높이가 높아질때마다 차이만큼 물 높이를 채운다.

h, w = map(int, input().split())
block = list(map(int, input().split()))

stack = []
volume = 0

for i in range(w):
    # 변곡점을 만나는 경우
    while stack and block[i] > block[stack[-1]]:
        # 스택에서 꺼냄
        top = stack.pop()

        if not len(stack):
            break

        # 이전과의 차이만큼 물 높이 처리
        distance = i - stack[-1] - 1
        waters = min(block[i], block[stack[-1]]) - block[top]
        volume += distance * waters

    stack.append(i)

print(volume)