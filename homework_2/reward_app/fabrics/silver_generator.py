from fabrics.item_fabric import ItemFabric
from products.silver import Silver


class SilverGenerator(ItemFabric):

    def create_item(self):
        return Silver()
