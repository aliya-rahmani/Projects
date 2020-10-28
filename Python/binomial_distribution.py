from numpy import random
seed = int(input("Enter seed: "))
num = int(input("Enter the number of trials: "))
prob = float(input("Enter the probability: "))
x = random.binomial(n=num, p=prob, size=seed)
print(x)
