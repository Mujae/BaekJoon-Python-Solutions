import sys
input_data = sys.stdin.read().split()
    
N = int(input_data[0])
students = list(map(int, input_data[1:]))

stack = []
order = 1  

for student in students:
    if student == order:
            order += 1
    else:
            
        stack.append(student)

    while stack and stack[-1] == order:
        stack.pop()
        order += 1

print("Nice" if not stack else "Sad")   
