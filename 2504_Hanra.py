# ([]())

# idea 
# 스텍을 이용해서 올바르게 괄호가 여닫히는지 확인하기.
# 분배법칙 => 처음 괄호가 열릴때 곱하는데, 닫힐 때 이전의 기호가 짝맞는 열림 괄호라면 더해주기 => []
# 근데 만약에 짝이 안맞는다면, 예를 들어 ([]) 의 )
# 그러면, ( 열릴때 1*2
# [ 열릴때 total = 1*2*3
# ] 닫힐때 결과값이 6이 되고, total = 1*2
# ) 닫힐때 total = 1 => 새출발 가능

def calculate():
    s = input()
    pairList = {'(' : ')', '[' : ']'}

    parenth = []
    total = 1
    result = 0


    for i in range(len(s)):
        p = s[i]
        if p == '(':
            parenth.append(p)
            total *= 2
        elif p == '[':
            parenth.append(p)
            total *= 3
        else:
            if len(parenth) == 0 or p != pairList[parenth[-1]]:
                return 0
            if p == ')':
                if s[i-1] == '(':
                    result += total
                total /= 2
            else:
                if s[i-1] == '[':
                    result += total
                total /= 3
            parenth.pop()
    # 이거때문에 계속 오류났음. ( 이것만 있는 경우, 확인해야지..
    if parenth:
        return 0
    return result

print(int(calculate()))