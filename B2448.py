from collections import deque
N = int(input())
q=[]
q.append([' ', ' ', '*', ' ', ' '])
q.append([' ', '*', ' ', '*', ' '])
q.append(['*', '*', '*', '*', '*'])
space = [' ', ' ', ' ']#이전 것들에 추가할 공

def Add_Star(a):
    global N
   
    if a==N//3:
        return
    l = len(q)
    for i in range(l):
        q.append(q[i] + [' '] + q[i])

    for i in range(l):
        q[i] = space*a + q[i] + space*a
    
    Add_Star(a*2)

Add_Star(1)

#문자열 덧셈은 계속 새로운 객체를 생성하여 느리지만 join은 미리 최종 문자열을 계산하고 진행하여 빠름 
print("".join(["".join(q[i])+"\n" for i in range(len(q))]))

