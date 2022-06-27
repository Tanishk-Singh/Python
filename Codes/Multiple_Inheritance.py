# Parent Class
class User():

    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')

# Children Classes


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):

        print(f'attacking with arrows: arrows left-{self.arrows}')


class HybridBorg(Archer, Wizard):

    def __init__(self, name, power, email, arrows):
        Wizard.__init__(self, name, power, email)
        Archer.__init__(self, name, arrows)


hb1 = HybridBorg('borgie', 50, 't@g', 100)
print(hb1.power)
