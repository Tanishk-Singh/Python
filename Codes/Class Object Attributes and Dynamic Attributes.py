# OOP
class PlayerCharacter:
    # Class Object Attribute
    membership = True

    def __init__(self, name, age):
        if (PlayerCharacter.membership):
            self.name = name
            self.age = age

    def shout(self):
        print(f'my name is {self.name}')

    def run(self, hello):
        print(f'{hello} my name is {self.name}')


player1 = PlayerCharacter('Tanishk', 25)
player2 = PlayerCharacter('Tom', 21)
player2.attack = 50
print(player2.shout())
print(player1.run('hi'))
