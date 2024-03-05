import sys

input = sys.stdin.readline

n, m = input().rstrip().split()
n=int(n)
if m=='Y':
    m=1
elif m=='F':
    m=2
else:
    m=3
sett = set()
for i in range(n):
    sett.add(input())

l = len(sett)
print(l//m)
