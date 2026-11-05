#anonymous and one-time function that you only use once.

# lambda param: manipulation(param)

my_list = [1, 2, 3]


print(list(map(lambda item: item * 2, my_list)))
print(my_list)