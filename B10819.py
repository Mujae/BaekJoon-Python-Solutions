
n = 9
a1, a2=0, 0
arr = [int(input()) for _ in range(n)]
 
for i in range(n):
    for j in range(i+1, n):
        if sum(arr) - (arr[i] + arr[j]) == 100:
            a1 = arr[i]
            a2 = arr[j]
            
arr.remove(a1)
arr.remove(a2)
 
arr.sort()
for i in range(7):
    print(arr[i])
