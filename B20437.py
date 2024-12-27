import sys

input = sys.stdin.readline

T = int(input())

#먼저 소문자 알파뱃들 위치를 파악해놓고 약간의 슬라이딩 윈도우로 해결
#속도개선가능 
for _ in range(T):
    W = input().rstrip()
    K = int(input())
    li = [[] for _ in range(26)]
    M1 = 10001
    M2 = 0

    for i in range(len(W)):
        li[ord(W[i])-97].append(i)
    
    if K == 1:
        print(1, 1)
        continue
    
    for i in range(26):
        l = len(li[i])
        if l==0 or l<K:
            continue

        for j in range(l):
            if j+K-1>l-1:
                break

            M1 = min(M1, li[i][j+K-1]-li[i][j]+1)
            M2 = max(M2, li[i][j+K-1]-li[i][j]+1)
        
    if M1 == 10001 or M2 == 0:
        print(-1)
    else:
        print(M1, M2)
