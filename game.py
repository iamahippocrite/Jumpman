import pygame
import sys

from jumpman_character import Jumpman
from level1 import Level
from settings import Settings

class JumpManGame:
    def __init__(self) -> None:
        '''Initialize the game and its resources.'''
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height), pygame.RESIZABLE)
        pygame.display.set_caption("Jump Man!")
        self.clock = pygame.time.Clock()
        self.delta_time = self.clock.tick(60)/1000
        self.screen.fill(self.settings.screen_bg_color)
        self.jumpman_character = Jumpman(self)
        self.level = Level(self)

    def _check_keydown_presses(self, event):
        """This function checks for keydown presses and events."""
        if event.key == pygame.K_q:
            pygame.quit()
            sys.exit()
        elif event.key == pygame.K_RIGHT:
            self.jumpman_character.moving_right_state = True
        elif event.key == pygame.K_LEFT:
            self.jumpman_character.moving_left_state= True
        elif event.key == pygame.K_UP and not self.jumpman_character.jumping_state:
            self.settings.jumpman_y_velocity = -self.settings.jumpman_jump_height
            self.jumpman_character.jumping_state = True


    def _check_keyup_presses(self, event):
        """This function checks for keyup presses and events."""
        if event.key == pygame.K_RIGHT:
            self.jumpman_character.moving_right_state = False
        elif event.key == pygame.K_LEFT:
            self.jumpman_character.moving_left_state= False 

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_presses(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_presses(event)


            self.screen.fill(self.settings.screen_bg_color)
            self.level.draw()
            self.jumpman_character.draw()
            self.jumpman_character.move()
            pygame.display.update()
            self.clock.tick(60)



if __name__ == "__main__":
    jm = JumpManGame()
    jm.run_game()
