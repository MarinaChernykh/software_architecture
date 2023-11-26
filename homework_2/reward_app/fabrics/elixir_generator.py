from fabrics.item_fabric import ItemFabric
from products.elixir import Elixir


class ElixirGenerator(ItemFabric):

    def create_item(self):
        return Elixir()
