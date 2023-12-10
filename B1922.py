#B1922 최소 스패닝 트리
import sys

def union_find(a, b): #루트(부모)를 찾아서 루트 번호가 더 작은 곳에 큰 루트번호를 붙임
    ah = get_parent(a)
    bh = get_parent(b)
    if ah>bh:
        parent[ah] = bh
    else:
        parent[bh] = ah

def get_parent(x):
    if parent[x]==x:#루트노드는 값이 루트의 번호
        return x
    parent[x] = get_parent(parent[x])
    return parent[x]


def same_parent(a,b):
    return get_parent(a) == get_parent(b)


input = sys.stdin.readline

N = int(input())
M = int(input())

li = [] # 간선리스트
parent = [i for i in range(N+1)]

for i in range(M):
    li.append(list(map(int, input().split())))

li = sorted(li, key = lambda x:x[2]) #크루스칼 알고리즘은 가중치가 작은 '간선'부터 택하기에 정
c=0
k=0
for v1, v2, l in li:
    if not same_parent(v1,v2):
        c+=1
        k+=l
        union_find(v1,v2)
        if c==N-1:
            break
print(k)
