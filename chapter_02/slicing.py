numbers = [10, 20, 30, 40, 50, 60]

# split at 2
print(numbers[:2])
print(numbers[2:])

bike = 'bicycle'
print(bike[::3])
print(bike[::-1])
print(bike[::-2])

# named slice
bio = "My name is Emiliyan"
NAME = slice(11, 19)
print(bio[NAME])

# assigning ot slices
numbers[1:3] = [2,3]
print(numbers)