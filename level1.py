import pygame

class Level:
    """This is a class to create a level"""
    def __init__(self, j_game) -> None:
        self.settings = j_game.settings
        self.screen = j_game.screen
        self.screen_rect = self.screen.get_rect()
        self.rect = pygame.Rect(0,self.settings.screen_height - 100 , self.settings.screen_width, 100 )
        
    def draw(self):
        pygame.draw.rect(self.screen, self.settings.floor_color, self.rect)



