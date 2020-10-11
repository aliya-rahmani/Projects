import numpy
from scipy import stats

n=int(input())
l=list(map(int, input().split()))
m=numpy.mean(l)
me=numpy.median(l)
mo=int(stats.mode(l)[0])

print("Mean= " + str(m))
print("Median= " + str(me))
print("Mode= " + str(mo))