import sys, copy
#입력
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
'''
li = copy.deepcopy(A)
l = len(li)
l2 = l
l3 = 1
#전에 감소를 탐지한 곳부터 다쉬 ㄱ
def check_decrease():
    global l, l3
    for k in range(l3,l):
        if li[k]<li[k-1]:
            l3 = k
            return False
    return True
#기존에서 맨 뒤는 pop하고 한단계씩 증가시켜서 비교하면 좀 더 빠르지 않을까?
for i in range(1,N):
    if check_decrease():
        print(i)
        break
    l-=1
    for j in range(l):
        if j+i<l2:
            li[j]=max(li[j],A[j+i])
'''    
    
#이번에는 미리 리스트를 탐방해서 해당수보다 작은 수들이 앞쪽으로 얼마나 있는지를 미리 계산하자
max_decrease_len=0
k=0
i=1
while i<N:
    if A[i]<A[i-1]:
        a=1
        for j in range(i+1,N):
            if A[j]>=A[i-1]:
                i=j
                break
            a+=1
        max_decrease_len = max(max_decrease_len, a)
        if max_decrease_len>=N//2:
            break
    i+=1
print(max_decrease_len+1)
        
