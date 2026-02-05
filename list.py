numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

filtered_numbers = [n for n in numbers if n <= 0]

print(filtered_numbers)




list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flattened_list = [item for sublist in list_of_lists for item in sublist]

print(flattened_list)