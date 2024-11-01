"""This is the Module for the settings of Jumpman."""

class Settings:
    def __init__(self) -> None:
        #Screen Settings
        self.screen_width = 1920
        self.screen_height = 1080
        self.screen_bg_color = (0, 191, 255)

        #Jumpman Settings
        self.jumpman_width = 50
        self.jumpman_height = 50
        self.jumpman_x_velocity = 700
        self.jumpman_jump_height = 120
        self.jumpman_y_velocity = 0

        #Level Settings
        self.floor_color = (51, 8, 0)
        self.gravity_velocity = 10

