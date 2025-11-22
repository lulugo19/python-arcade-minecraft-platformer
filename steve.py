import arcade
from animation import Animation

class Steve(arcade.Sprite):

    def __init__(self, **kwargs):
        super().__init__("steve_idle.png", **kwargs)
        self.animations = {
            "idle": Animation(self, ["steve_idle.png"]),
            "walk": Animation(self, ["steve_walk01.png", "steve_walk02.png"]),
            "pickaxe": Animation(self, ["steve_pickaxe01.png", "steve_pickaxe02.png"])
        }
        self.current_animation = "idle"

    def update(self, delta_time = 1 / 60, *args, **kwargs):
        self.animations[self.current_animation].update(delta_time)