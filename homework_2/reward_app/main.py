from random import shuffle

from fabrics.gold_generator import GoldGenerator
from fabrics.gem_generator import GemGenerator
from fabrics.silver_generator import SilverGenerator
from fabrics.amulet_generator import AmuletGenerator
from fabrics.elixir_generator import ElixirGenerator
from fabrics.ring_generator import RingGenerator
from fabrics.sword_generator import SwordGenerator


if __name__ == '__main__':
    generators = [
        GoldGenerator(), GemGenerator(), SilverGenerator(), AmuletGenerator(),
        ElixirGenerator(), RingGenerator(), SwordGenerator()
    ]
    quantities = [3, 1, 10, 10, 10, 10, 10]
    rewards = [
        genetator
        for genetator, quantity in zip(generators, quantities)
        for _ in range(quantity)
    ]
    shuffle(rewards)
    for reward in rewards:
        reward.create_item().open()
