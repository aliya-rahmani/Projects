from numpy import random
seed = int(input("seed:"))
num = int(input("n:"))
prob = float(input("p:"))
x = random.binomial(n=num, p=prob, size=seed)
print(x)
