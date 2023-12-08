import sys

input = sys.stdin.readline

# 간선들을 가중치로 정렬
# 간선을 값이 적은 것부터 추가
# 추가할 때 정점을 고려해서 추가하는디 집합하나를 만들어놓고 추가
# 만약 추가하는 정점 두 개가 둘 다 집합에 속해 있으면 그건 사이클을 만드니 추방
n, m  = map(int, input().split())

s = set()#정점관리집합

li = [] #간선관리 리스트
for i in range(m):
    li.append(list(map(int, input().split())))
li = sorted(li, key = lambda x:-x[2])
parent = [i for i in range(n+1)]
def get_parent(x):
    if parent[x]==x:
        return x
    parent[x] = get_parent(parent[x])
    return parent[x]

def union_parent(p, q):
    p = get_parent(p)
    q = get_parent(q)

    if p>q:
        parent[p] = q
    else:
        parent[q] = p
def same_parent(p, q):
    return get_parent(p) == get_parent(q)

l=0
k=0
while l<n-1:
    a, b, c = li.pop()
    
    if not same_parent(a,b):
        k+=c
        union_parent(a, b)
        l+=1
print(k)
