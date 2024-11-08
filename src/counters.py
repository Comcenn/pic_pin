from typing import List
import arcade

from config import Config


class Counter(arcade.Sprite):
    image_path: str

    def __init__(self, config: Config) -> None:
        super().__init__(self.image_path, config.COUNTER_SCALE)


class Hero(Counter):
    """A generic Hero counter meant for players."""
    image_path = "assets/hero.png"


class Knight(Counter):
    """A Heroic Knight counter"""
    image_path = "assets/knight.png"


class Orc(Counter):
    """A generic Enemy counter meant for enemies."""
    image_path = "assets/orc.png"


COUNTER_REGISTRY: List[Counter] = [
    Hero,
    Knight,
    Orc
]
