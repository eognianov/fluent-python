from collections import namedtuple

coordinates = (33.92, -118.231)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', 12312341), ('BGN', '123131231')]

for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

for country, _ in traveler_ids:
    print(country)

a, b, *rest = range(5)
print(a, b, rest)

a, *rest, b = range(5)
print(a, rest, b)

accounts = [
    ('personal', (1234, 10)),
    ('company', (2234, 20))
]

for account, (debit, credit) in accounts:
    print(f'{account}: +{debit} -{credit}')

# Named tuples
City = namedtuple('City', ['name', 'country'])

sofia = City('Sofia', 'BG')

print(City._fields)
kyustendil_data = ('Kyustendil', 'BG')
kyustendil = City._make(kyustendil_data)
print(kyustendil.name)
print(kyustendil._asdict())