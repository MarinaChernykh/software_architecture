from fabrics.item_fabric import ItemFabric
from products.gold import Gold


class GoldGenerator(ItemFabric):

    def create_item(self):
        return Gold()
