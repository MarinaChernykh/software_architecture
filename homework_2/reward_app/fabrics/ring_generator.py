from fabrics.item_fabric import ItemFabric
from products.ring import Ring


class RingGenerator(ItemFabric):

    def create_item(self):
        return Ring()
