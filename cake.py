class Cake:
    def __init__(self, cakes):
        self.cakes = cakes

    def __str__(self):
        print(self.cakes)

class Player:
    def __init__(self, name):
        self.name = name


    def step(self):
        self.take = 0
        self.take = int(input('Введите колиичетво кусков, желаемых вами:'))

        self.cakes = self.cakes - self.take

    def game(self):
        pass


cakes = 12
player_1 = Player('Vova')
player_2 = Player('Somebody')

while cakes > 1:
    player_1.step()
    Cake()
    player_2.step()



