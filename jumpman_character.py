import pygame

class Jumpman:

    def __init__(self, j_game) -> None:
        '''Initialize the player character and its starting position'''
        super().__init__()
        self.settings = j_game.settings
        self.screen = j_game.screen 
        self.delta_time = j_game.delta_time
        self.screen_rect = j_game.screen.get_rect()
        self.rect = pygame.Rect(0, self.settings.screen_height - 150, self.settings.jumpman_width, self.settings.jumpman_height)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_right_state = False
        self.moving_left_state = False
        self.jumping_state = False

    def draw(self):
        pygame.draw.rect(self.screen, (255, 0, 0), self.rect)

    def move(self):
        if self.moving_right_state and self.rect.right < self.settings.screen_width:
            self.x += self.settings.jumpman_x_velocity * self.delta_time
            self.rect.x = self.x
        if self.moving_left_state and self.rect.left > 0:
            self.x -= self.settings.jumpman_x_velocity * self.delta_time
            self.rect.x = self.x
        if self.jumping_state: 
            self.settings.jumpman_y_velocity += self.settings.gravity_velocity
            self.rect.y += self.settings.jumpman_y_velocity
            if self.rect.bottom >= self.settings.screen_height - 100:
                self.rect.bottom = self.settings.screen_height - 100
                self.settings.jumpman_y_velocity = 0
                self.jumping_state = False
            

