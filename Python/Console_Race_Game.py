m=[]



for i in range(0,5,1):
    a=[]
    for j in range(0,3,1):
        a.append('  ^  ')
    m.append(a)


m[4][0]='  X  '
m[4][1]='  Y  '
m[4][2]='  Z  '



for x in range(0,5,1):
    for y in range(0,3,1):
        print([m[x][y]], end=" ")
    print("\r")
print('\n''\n')



import random
b=4
d=4
e=4
for i in range(1,7,1):
    if b>=0:
        print('X (I) :',i)
        a = random.randint(1, 3)
        print('X (a) :', a)
        A=b-1
        B=b-a-1
        if a > b:
            A=B
        for j in range(A, B, -1):  # b=b+1#b-a-1
            m[j][0] = '  X  '
        b = b - a
        for x in range(0, 5, 1):
            for y in range(0, 3, 1):
                print([m[x][y]], end=" ")
            print("\r")
        print('\n''\n')
        if m[0][0] == '  X  ':
            print('X is winner ')
            break



    if d >= 0:
        print('Y (I) :', i)
        a = random.randint(1, 3)    ###########3  B=D
        print('Y (a) :', a)
        C=d-1
        D=d-a-1
        if a > d:
            C=D  # b = b - a - 1
        for j in range(C, D, -1):  # b=b+1#b-a-1
            m[j][1] = '  Y  '
        d = d - a
        for x in range(0, 5, 1):
            for y in range(0, 3, 1):
                print([m[x][y]], end=" ")
            print("\r")
        print('\n''\n')
        if m[0][1] == '  Y  ':
            print('Y is winner ')
            break


    if e >= 0:
        print('Z (I) :', i)
        a = random.randint(1, 3)
        print('z (a) :', a)
        E=e-1
        F=e-a-1
        if a > e:
            E=F  # b = b - a - 1
        for j in range(E, F, -1):  # b=b+1#b-a-1
            m[j][2] = '  Z  '
        e = e - a
        for x in range(0, 5, 1):
            for y in range(0, 3, 1):
                print([m[x][y]], end=" ")
            print("\r")
        print('\n''\n')
        if m[0][2] == '  Z  ':
            print('Z is winner ')
            break
        print('####   END   ###')




