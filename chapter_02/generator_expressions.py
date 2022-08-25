import array

symbols = '$¢£¥€'

symbols_generator = (ord(symbol) for symbol in symbols)
print(next(symbols_generator))
print(next(symbols_generator))
print(next(symbols_generator))

tuple_from_generator = tuple(ord(symbol) for symbol in symbols)
print(tuple_from_generator)
array_from_generator = array.array('I', (ord(symbol) for symbol in symbols))
print(array_from_generator)

# Cartesian product as generator
colors = ['black', 'white']

sizes = ['S', 'M', 'L']

tshirt_generator = ((color, size) for color in colors for size in sizes)
print(next(tshirt_generator))
print(next(tshirt_generator))
print(next(tshirt_generator))
print(next(tshirt_generator))
print(next(tshirt_generator))