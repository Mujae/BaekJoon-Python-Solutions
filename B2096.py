import sys

input = sys.stdin.readline

#전에 수 확인해서 작은거 더해주는 방향으로

N = int(input())

min_arr=[0]*3
max_arr=[0]*3

for i in range(N):
    li = list(map(int,input().split()))
    min_arr = [li[0]+min(min_arr[0],min_arr[1]), li[1]+min(min_arr[0],min_arr[1],min_arr[2]), li[2]+min(min_arr[1],min_arr[2])]
    max_arr = [li[0]+max(max_arr[0],max_arr[1]), li[1]+max(max_arr[0],max_arr[1],max_arr[2]), li[2]+max(max_arr[1],max_arr[2])]

print(max(max_arr), min(min_arr))
