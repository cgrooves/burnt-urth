""" Sprite Sample Program """

import random
import pymunk
import arcade
from weapons import Weapon
import tank
from config import TurretConfig


# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that hold sprit lists.
        self.player_list = None
        self.bullet_list = None

        # Setup up player info
        self.tank_sprite = None

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

    def setup(self):
        """ Set up the game and initialize the variables """

        self.tank = tank.Tank("player", self, pymunk.Vec2d(50,50), arcade.color.AERO_BLUE)

    def on_draw(self):
        arcade.start_render()
        self.tank.draw()

    def on_update(self, delta_time):
        """ Update game state for game objects """

        # Make the active tank update
        self.tank.on_update()

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()