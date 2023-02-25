l1 = []
l2 = []

# 주어진 괄호를 앞에서부터 하나하나 보자.
for s in input():
    #  이 셋 중 하나라면 l1에만 집어넣는다.
    if s in '([':
        l1.append(s)
        l2.append(0)
        continue
    # 닫는 괄호들이면 타겟 설정하고 계산을 위한 값도 설정.
    if s == ')':
        target = '('
        value = 2
    if s == ']':
        target = '['
        value = 3
    # l1에 마지막에 들어간 것이 타겟이 아니면 끝
    if not l1 or l1[-1] != target:
        l2 = [0]
        break
    if len(l1) < len(l2):
        r = l2.pop()
        if r:
            value *= r
    l2[-1] += value
    l1.pop()

print(l2[0])