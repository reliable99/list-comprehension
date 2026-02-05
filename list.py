numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

filtered_numbers = [n for n in numbers if n <= 0]

print(filtered_numbers)




list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flattened_list = [item for sublist in list_of_lists for item in sublist]

print(flattened_list)



result = [
    (i, 1, i, i**2, i**3, i**4, i**5)
    if i != 0 else (0, 1, 0, 0, 0, 0, 0)
    for i in range(11)
]

print(result)


countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

flattened = [
    [country.upper(), country[:3].upper(), capital.upper()]
    for [(country, capital)] in countries
]

print(flattened)


countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

result = [
    {'country': country.upper(), 'city': city.upper()}
    for [(country, city)] in countries
]

print(result)


names = [
    [('Asabeneh', 'Yetayeh')],
    [('David', 'Smith')],
    [('Donald', 'Trump')],
    [('Bill', 'Gates')]
]

result = [
    f"{first} {last}"
    for [(first, last)] in names
]

print(result)