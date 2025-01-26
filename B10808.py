s = input().rstrip()
li = [0]*26

for i in range(len(s)):
    li[ord(s[i])-97]+=1
    
print(*li)
