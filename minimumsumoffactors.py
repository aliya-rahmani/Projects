def findMinSum(num): 
    sum = 0
    i = 2
    while(i * i <= num): 
        while(num % i == 0): 
            sum += i 
            num /= i 
        i += 1
    sum += num 
    return sum

num =int(input("enter the number for which you want to find minimum sum of factor"))
print (findMinSum(num)) 
  
