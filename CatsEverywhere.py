class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self._name = name #private variable as a convention
        self._age = age

    def oldest_cat(*args):
        return max(args)

    @classmethod
    def adding_things(cls, age1, age2):
        return age1 + age2
    @staticmethod
    def adding_things2(age1, age2):
        return age1 + age2


# Make sure not to override a private variable based on the agreed convention. There is no really privacy in Python.

cat1= Cat('cat1', 23)
cat2 = Cat('cat2', 34)
cat3 = Cat('cat3', 73)




print(f'Oldest cat is {Cat.oldest_cat(cat1.age, cat2.age, cat3.age)} years old')