class PlayerCharacter:

    # constructor method - accept whatever is after self as the character.
    # The self.name for example is the attribute.
    def __init__(self, name):
        self.name = name


    def run(self):
        print("run")

player1 = PlayerCharacter("Priscilla")
player2 = PlayerCharacter("Tom")

print(player1.name)
print(player2.name)