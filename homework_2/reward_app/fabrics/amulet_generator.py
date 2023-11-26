from fabrics.item_fabric import ItemFabric
from products.amulet import Amulet


class AmuletGenerator(ItemFabric):

    def create_item(self):
        return Amulet()
