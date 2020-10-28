s = input("Enter a string: ")
length = len(s)
emp = ''
ls =[]
for i in range(length):
    if i+1!=length:
        if s[i+1].lower()>=s[i].lower():
            if s[i] not in emp:
                emp = emp + s[i]
            emp = emp+s[i+1]
            ls.append(emp)
        else:
            ls.append(emp)
            emp = ''
for j in ls:
    print(max(ls))
    break
