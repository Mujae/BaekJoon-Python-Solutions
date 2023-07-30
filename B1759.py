def qSort(li,l1,l2):
    if l1>=l2:
        return 
    t=l1 # 피봇(기준)
    a=l1+1
    b=l2
    while a<=b:
        while a<=l2 and li[a]<=li[t]:
            a+=1
        while b>l1 and li[b]>=li[t]:
            b-=1
        if a>b:# 이식 덕분에 피봇이 제 자리를 찾아감.
            li[b], li[t] = li[t], li[b]
        else:
            li[b], li[a] = li[a], li[b]
    qSort(li,l1,b-1)
    qSort(li,b+1,l2)
    
def dfs(n):
    global stack, ai
    if len(stack)==l:#원하는 길이 만족
        k=0
        for w in stack:
            if ord(w) in ai:# at least 1 vowel
                k=1
                break
        if k==1:
            k=0
            for w in stack:# at least 2 consonant
                if ord(w) not in ai:
                    k+=1
                    if k==2:
                        break
            if k==2:
                for w in range(l):
                    print(stack[w], end="")
                print()
        return
    for j in range(n+1,c):
        if li[j] not in stack:
            stack.append(li[j])
            dfs(j)
            stack.pop()
l,c = map(int, input().split())
ai = [97, 101, 105, 111, 117]
li = list(input().rstrip().split()) #사전순으로 출력 기기스
qSort(li,0,c-1)
stack=[]
for i in range(c):
    stack.append(li[i])
    dfs(i)
    stack.pop()
