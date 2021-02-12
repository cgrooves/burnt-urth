
import arcade
from pymunk import Vec2d

TANK_SIZE = 50
TANK_TURRET_LENGTH = 50
TANK_STARTING_ANGLE_DEG = 45
TURRET_ANGLE_MAX = 180
TURRET_ANGLE_MIN = 0
TURRET_WIDTH = 5
TURRET_OFFSET_Y = 5
TURRET_SPEED = 2

class Tank:

    def __init__(self, x: float, y: float, color: arcade.color):
        self.size = TANK_SIZE
        self.position = Vec2d(x,y)
        self.color = color
        self.turretAngleDeg = TANK_STARTING_ANGLE_DEG
        self.turretLength = TANK_TURRET_LENGTH
        self.moveTurret = 0

    def draw(self):
        # Draw tank body
        arcade.draw_arc_filled(
            center_x=self.position.x,
            center_y=self.position.y,
            width=self.size,
            height=self.size,
            color=self.color,
            start_angle=0.0,
            end_angle=180
        )
        # Draw turret
        # Calculate turret end point
        turretPosition = Vec2d(self.turretLength, 0)
        turretPosition.rotate_degrees(self.turretAngleDeg)
        arcade.draw_line(
            start_x=self.position.x,
            start_y=self.position.y,
            end_x=turretPosition.x + self.position.x,
            end_y=turretPosition.y + self.position.y,
            color=self.color,
            line_width=TURRET_WIDTH
        )
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.moveTurret += TURRET_SPEED
        if key == arcade.key.RIGHT:
            self.moveTurret -= TURRET_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.moveTurret -= TURRET_SPEED
        if key == arcade.key.RIGHT:
            self.moveTurret += TURRET_SPEED

    def on_update(self):
        if self.moveTurret != 0:
            self.turretAngleDeg += self.moveTurret
        if self.turretAngleDeg > TURRET_ANGLE_MAX:
            self.turretAngleDeg = TURRET_ANGLE_MAX
        elif self.turretAngleDeg < TURRET_ANGLE_MIN:
            self.turretAngleDeg = TURRET_ANGLE_MIN