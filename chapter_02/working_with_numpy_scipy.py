import numpy

a = numpy.arange(12)

print(a)
print(type(a))
print(a.shape)

a.shape = 3, 4
print(a)
print(a[2])
print(a[2, 1])

# Get column from the matix
print(a[:, 1])

print(a.transpose())
