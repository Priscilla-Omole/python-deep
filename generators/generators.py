'''
difference between a list using for loop and using range. It does not actually keep any of the values in the memory.
 But using a for loop keeps values in the memory before you can use it.

 Every generator is an iterable but not every iterable is a generator.
'''

def generator_func(num):
    for i in range(num):
        yield i*2

#yield pauses the function. Give i and until we tell it to go again, it generates again. Holding one item in memory at a time.

g= generator_func(100)
next(g)
next(g)
print(next(g))



#
# for item in generator_func(1000):
#     print(item)