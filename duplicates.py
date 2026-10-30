some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicate_list = []

for item in some_list:
    if some_list.count(item) > 1:
        if item not in duplicate_list:
            duplicate_list.append(item)
print(duplicate_list)