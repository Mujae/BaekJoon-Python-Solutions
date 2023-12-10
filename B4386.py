import sys

def union_find(a, b):
    a = get_parent(a)
    b = get_parent(b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x])
    return parent[x]

def same_parent(a, b):
    return get_parent(a) == get_parent(b)

input = sys.stdin.readline

n = int(input())
li1 = []#별자리 좌표 리스트
parent = [i for i in range(n+1)]
for i in range(n):
    li1.append(list(map(float, input().split())))

li2 = []#간선 리스트 (별자리 간의)

#별 간의 경로를 다 구해 어차피 제한 시간 2초에 n은 최대 100이라 괜찮음
for i in range(n):
    for j in range(n):
        if i!=j:
            li2.append([i+1,j+1,round(((li1[i][0]-li1[j][0])**2+(li1[i][1]-li1[j][1])**2)**0.5,3)])
        
li2 = sorted(li2, key = lambda x:x[2])

l=0#간선n-1개 되면 탈출
k=0#가중치
for v1, v2, e in li2:
    if not same_parent(v1,v2):
        k+=e
        l+=1
        union_find(v1,v2)
        if l==n-1:
            break
print(round(k,2))
