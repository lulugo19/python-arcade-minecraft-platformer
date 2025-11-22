import arcade

class Animation:

    def __init__(self, sprite: arcade.Sprite, textures: list[str], fps = 5):
        self.sprite = sprite
        self.textures = list(map(arcade.load_texture, textures))
        self.texture_index = 0
        self.fps = 5
        self.current_time = 0

    def update(self, delta_time: float):
        self.sprite.texture = self.textures[self.texture_index]
        self.current_time += delta_time
        if self.current_time > (1 / self.fps):
            self.current_time = 0
            self.texture_index = (self.texture_index + 1) % len(self.textures)

