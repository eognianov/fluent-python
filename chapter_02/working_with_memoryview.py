import array

numbers = array.array('h', [-2, -1, 0, 1, 2])
# Create memory view
memv = memoryview(numbers)
print(len(memv))
print(memv[0])

# Create memv_oct from casting elements to unsigned char
memv_oct = memv.cast('B')
print(memv.tolist())
# Assign new value in the memory view
memv_oct[5] = 4
print(numbers)
