#anonymous and one-time function that you only use once.
from functools import reduce

# lambda param: manipulation(param)

my_list = [1, 2, 3]

print(list(filter(lambda item: item % 2 !=0, my_list)))
print(reduce(lambda acc, item: acc + item, my_list))
print(my_list)