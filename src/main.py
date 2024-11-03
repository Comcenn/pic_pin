import arcade

# Constants
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
SCREEN_TITLE = "PicPin - Dungeon Tool"


class PicPinWindow(arcade.Window):
    """Main application class"""

    def __init__(self) -> None:
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.color.ANTIQUE_BRONZE)
    
    def setup(self) -> None:
        """Method to setup application"""
        pass

    def on_draw(self) -> None:
        """Render the screen"""
        # Clear the screen
        self.clear()
    
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> None:
        """Called when user clicks a mouse button"""
        pass

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int) -> None:
        """Called when user clicks a mouse button"""
        pass

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int) -> None:
        """Called when user moves mouse"""
        pass