from argparse import ArgumentParser, Namespace
from typing import List

import arcade
import arcade.csscolor
import arcade.csscolor

from config import Config
from counters import COUNTER_REGISTRY, Counter


class PicPinWindow(arcade.Window):
    """Main application class"""

    def __init__(self, config: Config) -> None:
        super().__init__(config.SCREEN_WIDTH, config.SCREEN_HEIGHT, config.SCREEN_TITLE, resizable=True)

        if config.map_path:
            self.map_texture = arcade.load_texture(config.map_path)


        self.app_config = config

        # collection of all the sprites
        self.all_sprites = arcade.SpriteList()
        self.held_sprites: List[arcade.Sprite] = []
        self.held_sprites_original_position: List[arcade.Point] = []
        self.mat_list = arcade.SpriteList()

        arcade.set_background_color(arcade.color.AMAZON)
    
    def setup(self) -> None:
        """Method to setup application"""

        for i, counter in enumerate(COUNTER_REGISTRY):
            pile = arcade.SpriteSolidColor(
                self.app_config.MAT_WIDTH,
                self.app_config.MAT_HEIGHT,
                arcade.csscolor.DARK_OLIVE_GREEN
                )
            pile.position = self.app_config.START_X + i * self.app_config.X_SPACING, self.app_config.BOTTOM_Y
            self.mat_list.append(pile)
            for _ in range(10):
                piece: Counter = counter(self.app_config)

                piece.position = self.app_config.START_X + i * self.app_config.X_SPACING, self.app_config.BOTTOM_Y
                self.all_sprites.append(piece)

    def on_draw(self) -> None:
        """Render the screen"""
        # Clear the screen
        self.clear()

        if self.map_texture:
            width, hieght = self.get_size()
            arcade.draw_lrwh_rectangle_textured(0, 0, width, hieght, self.map_texture)

        # Draw mats
        self.mat_list.draw()

        # Draw all the sprites
        self.all_sprites.draw()

    def put_on_top(self, counter: arcade.Sprite) -> None:
        self.all_sprites.remove(counter)
        self.all_sprites.append(counter)
    
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> None:
        """Called when user clicks a mouse button"""
        
        # Get any sprites we have clicked on
        sprites = arcade.get_sprites_at_point((x, y), self.all_sprites)

        if len(sprites) > 0:

            top_card = sprites[-1]

            if button == arcade.MOUSE_BUTTON_LEFT:
                self.held_sprites.append(top_card)
                self.held_sprites_original_position.append(top_card.position)

                self.put_on_top(top_card)
            elif button == arcade.MOUSE_BUTTON_RIGHT:
                # getting the index in registry which corresponds to which pile it is in
                idx = COUNTER_REGISTRY.index(top_card.__class__)
                # Reset counters position
                top_card.position = self.app_config.START_X + idx * self.app_config.X_SPACING, self.app_config.BOTTOM_Y

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int) -> None:
        """Called when user clicks a mouse button"""
        if len(self.held_sprites) == 0:
            return None
        
        self.held_sprites.clear()
        self.held_sprites_original_position.clear()

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int) -> None:
        """Called when user moves mouse"""
        for sprite in self.held_sprites:
            sprite.center_x += dx
            sprite.center_y += dy


def parse_cmd_line_args() -> Namespace:
    parser = ArgumentParser(
        prog="Pic Pinner",
        description="Load a picture and pin counters to parts of it...",
        )
    parser.add_argument("image")
    return parser.parse_args()


def main() -> None:
    """Entry into program"""
    args = parse_cmd_line_args()
    config = Config(args)
    window = PicPinWindow(config)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
