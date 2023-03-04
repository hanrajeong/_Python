# KMP algorithm question
S = input()
P = input()

# see if P is the partial string of S
# make the pattern with the input string P
table = [0] * len(P)
j = 0
# baekjoon
# oone
# 0
for i in range(1, len(P)):
    while j > 0 and P[i] != P[j]:
        j = table[j-1]
    if P[i] == P[j]:
        j += 1
        table[i] = j

j = 0
flag = False
for i in range(len(S)):
    while j > 0 and P[j] != S[i]:
        j = table[j-1]
    if P[j] == S[i]:
        j += 1
        if j == len(P):
            print(1)
            flag = True
            break

if not flag:
    print(0)