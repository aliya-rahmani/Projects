userInp = int(input("please enter your number: "))
myList = []

while userInp > 1:
    myList.append(str(userInp % 2))
    userInp = userInp // 2
myList.append(str(userInp))
myList.reverse()
output = " ".join(myList)
print(output)
