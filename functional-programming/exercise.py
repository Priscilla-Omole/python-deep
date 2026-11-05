from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def capitalize(item):
    return item.capitalize()

def pass_mark(item):
    return item > 50

print(list(map(capitalize, my_pets)))
print(list(zip(my_strings, sorted(my_numbers))))
print(list(filter(pass_mark, scores)))
