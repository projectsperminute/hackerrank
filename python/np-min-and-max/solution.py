import numpy

n,m = map(int,input().split())
array = []

for i in range(n):
    tmp = list(map(int,input().split()))
    array.append(tmp)
np_array = numpy.array(array)

print(numpy.max(numpy.min(np_array, axis = 1)))