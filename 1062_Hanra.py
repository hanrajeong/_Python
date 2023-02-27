import collections
answer = 0

[N, K] = list(map(int, input().split(" ")))
word = []

if K < 5:
    print(0)
    exit()
if K >= 26:
    print(N)
    exit()

for _ in range(N):
    w = input()
    if len(w) == 8 and K == 6:
        print(0)
        exit()
    word.append(dict(collections.Counter(w[4:-4])))

wordList = []

for w in word:
    l = sorted(list(w.keys()))
    # if 'a' in l: l.remove('a')
    # if 'n' in l: l.remove('n')
    # if 't' in l: l.remove('t')
    # if 'c' in l: l.remove('c')
    # if 'i' in l: l.remove('i')
    wordList.append(l)

char = [0] * 26
for w in 'antic':
    char[ord(w) - ord('a')] = 1
    
def dfs(a, letterCtn):
    global answer
    if letterCtn == K - 5:
        readingWord = 0
        for word in wordList:
            flag = True
            for w in word:
                if char[ord(w) - ord('a')] != 1:
                    flag = False
                    break
            if flag:
                readingWord += 1
        answer = max(answer, readingWord)
        return
    # prevLetter = letter
    # prevLetterCtn = letterCtn
    # if i< len(wordList) and (letterCtn + len(wordList[i])) <= K - 5:
    #     for w in wordList[i]:
    #         letter.append(w)
    #         letterCtn += 1
    # dfs(i+1, prevLetter, prevLetterCtn)
    # dfs(i+1, letter, letterCtn)
    for i in range(a, 26):
        if char[i] == 0:
            char[i] += 1
            dfs(i, letterCtn+1)
            char[i] -= 1
        
dfs(0, 0)
print(answer)
