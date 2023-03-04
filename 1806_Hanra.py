length, aim = map(int, input().split())
num = list(map(int, input().split()))

left, right = 0, 0
total = 0
result = float("inf")
flag = False

# pointer right will move to the right by one step,
# increase the total sum and see if it exceeds the aim
# and let's see whether move the left pointer makes the problem and compare the length
while True:
    # 
    # print(left, right)
    if total >= aim:
        result = min(result, right - left)
        flag = True
        total -= num[left]
        left += 1
    elif right >= length:
        break
    # if the sum exceeds the goal
    else:
        total += num[right]
        right += 1
        

if not flag:
    print(0)
else:
    print(result)