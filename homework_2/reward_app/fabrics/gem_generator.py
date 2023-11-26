from fabrics.item_fabric import ItemFabric
from products.gem import Gem


class GemGenerator(ItemFabric):

    def create_item(self):
        return Gem()
