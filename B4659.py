import sys

input = sys.stdin.readline

# 모음 한 개 반드시 포함
# 모음이나 자음이 연속으로 3번 나오면 안됨
# 같은 알파뱃이 연속으로 나오면 안되지만, 예외적으로 ee와 oo는 허용함.

mo = ['a','i','o','u','e']

while True:
    k=0#accept or not accept
    a = input().rstrip()
    if a=='end':
        break
    count_mo=0# 모음 카운트
    count_mo_con=0# 연속 모음 카운트
    count_ja_con=0# 연속 자음 카운트
    for i in range(len(a)):
        if a[i] in mo:
            count_mo+=1
            count_ja_con=0
            count_mo_con+=1
            if count_mo_con==3:
                k=1
                break
        else:
            count_ja_con+=1
            count_mo_con=0

            if count_ja_con==3:
                k=1
                break
        if i>0:
            if a[i]==a[i-1]:
                if a[i]!='e' and a[i]!='o':
                    k=1
                    break
    print('<',end="")
    print(a, end="")
    print('>', end=" ")
    if k==0 and count_mo>0:
        print('is acceptable.')
    else:
        print('is not acceptable.')
