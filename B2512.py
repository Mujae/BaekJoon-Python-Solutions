import sys

input = sys.stdin.readline

N = int(input())
li = list(map(int,input().split()))
M = int(input())

s=sum(li)
if s<=M:
    print(max(li))
else:
    a=min(li)
    b=max(li)
    m=0#최대상한
    li2 = [i for i in range(b+1)]
    l=len(li2)
    i=0
    j=l-1
    #이분탐색
    #이번 순서의 값을 리스트들에서 빼보고 어디로 갈지 결정
    while True:
        mi=(j-i)//2+i
        if i==mi or j==mi or j==i:
            m=max(m,li2[mi])
            break
        si=0
        for k in li:
            if k<=li2[mi]:
                si+=k
            else:
                si+=li2[mi]
        if si==M:
            m=li2[mi]
            break
        elif M>si:
            i=mi
            m=max(li2[mi],m)
        else:
            j=mi

    print(m)
