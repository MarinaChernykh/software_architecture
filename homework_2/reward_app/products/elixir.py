from products.game_item import GameItem


class Elixir(GameItem):

    def open(self):
        print('Elixir is found')
