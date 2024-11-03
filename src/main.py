from typing import List
import arcade

# Constants
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
SCREEN_TITLE = "PicPin - Dungeon Tool"
COUNTER_SCALE = 0.6


class Counter(arcade.Sprite):
    """Counter to represent players, NPC's and enemies"""

    def __init__(self) -> None:
        super().__init__(f"assets/hero.png", COUNTER_SCALE)

class PicPinWindow(arcade.Window):
    """Main application class"""

    def __init__(self) -> None:
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # collection of all the sprites
        self.all_sprites = arcade.SpriteList()
        self.held_sprites: List[arcade.Sprite] = []
        self.held_sprites_original_position = []

        arcade.set_background_color(arcade.color.ANTIQUE_BRONZE)
    
    def setup(self) -> None:
        """Method to setup application"""
        # Create one counter first and put in middle of screen
        counter = Counter()
        counter.position = self.width / 2, self.height / 2

        self.all_sprites.append(counter)

    def on_draw(self) -> None:
        """Render the screen"""
        # Clear the screen
        self.clear()

        # Draw all the sprites
        self.all_sprites.draw()
    
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> None:
        """Called when user clicks a mouse button"""
        
        # Get any sprites we have clicked on
        sprites = arcade.get_sprites_at_point((x, y), self.all_sprites)

        if len(sprites) > 0:

            self.held_sprites.extend(sprites)
            self.held_sprites_original_position.extend(position.position for position in sprites)

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


def main() -> None:
    """Entry into program"""
    window = PicPinWindow()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
