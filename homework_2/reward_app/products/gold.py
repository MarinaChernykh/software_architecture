from products.game_item import GameItem


class Gold(GameItem):

    def open(self):
        print('Gold is found')
