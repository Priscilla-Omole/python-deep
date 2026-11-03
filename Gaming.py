class PlayerCharacter:
    # this is a class object attribute but this is not dynamic and all the objects instiatied has access to it.
    membership = True

    # constructor method - accept whatever is after self as the character.
    # The self.name for example is the attribute.
    def __init__(self, name, age):
        if self.membership:
            self.name = name
            self.age = age #attributes


    def run(self):
        print(f"{self.name} is going to ride.")

player1 = PlayerCharacter("Priscilla", 44)
player2 = PlayerCharacter("Tom", 21)

print(player1.run())
print(player2.run())