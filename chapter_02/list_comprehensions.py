symbols = '$¢£¥€'
codes = []

for symbol in symbols:
    codes.append(ord(symbol))
print(codes)

codes = [ord(symbol) for symbol in symbols]
print(codes)

# difference between list comprehensions and filter/map
beyond_ascii = [ord(symbol) for symbol in symbols if ord(symbol) > 127]
print(beyond_ascii)

beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)

# Cartesian product
colors = ['black', 'white']

sizes = ['S', 'M', 'L']

t_shirts = [(color, size) for color in colors for size in sizes]

print(t_shirts)

