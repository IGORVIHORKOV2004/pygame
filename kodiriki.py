import pygame

r = pygame.Rect(x, y)
class Food:
    def __init__(self,name_image):#конструктор.Создание свойств
        self.image = pygame.image.load(name_image)# создание картинки
        rect=self.image.get_rect()# создание прям по границам картинки
        self.x=rect.x# координата х для картинки
        self.y=rect.y# координата у для картинки

    def draw_image(self):
        screen.blit(self.image(self.x,self.y))

    def move_food(self):
        self.y+=2
    def move_plate(self):
        keys = pygame.key.get_pressed()
        if  keys[pygame.K_LEFT]:
            self.x -= 3
        elif keys[pygame.K_RIGHT]:
            self.x += 3



plate=Food('plate')
def draw_image(self):
    while True:  # игрововй таймер
        
        clock.tick(40)
        plate.draw_image()
