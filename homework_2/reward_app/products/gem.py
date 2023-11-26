from products.game_item import GameItem


class Gem(GameItem):

    def open(self):
        print('Gem is found!')
