s = input().rstrip()
word = input().rstrip()

c = 0
i = 0

while i < len(s):
    if s[i:i+len(word)] == word:
        c += 1
        i += len(word)  
    else:
        i += 1  
print(c)
