import sys
input = sys.stdin.readline

#자주 맨 앞
#길이가 길수록 앞
#사전순으로
#M 이상이만 저장

#아래의 방법 말고 단어 정렬을 먼저 하고, 갯수 카운팅하는 방법이 더 빠름
N, M = map(int, input().split())
li=set()
li2=dict()
for i in range(N):
    word = input().rstrip()
    l = len(word)
    if l>=M:
        try:
            li2[word][0]+=1
        except:
            li2[word]=[1,l]

            
li3=[]
for i, j in li2.items():
    li3.append([i,j[0],j[1]])

li3 = sorted(li3, key=lambda x: (-x[1],-x[2],x[0]))

for a,_,_ in li3:
    print(a)
