import pygame

pygame.init()# обязательная команда
window_size=(300,300)
screen=pygame.display.set_mode(window_size)#создание экрана с размерами 300 на 300
pygame.display.set_caption("МОЯ ИГРА!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
background_color=(0,0,255)#создание цвета
screen.fill(background_color)# заливка зеднего фона цветом из строки 7
clock=pygame.time.Clock()# объект- таймер
card = pygame.Rect(100, 125, 100, 50)
pygame.draw.rect(screen, (255, 255, 255), card)

while True: # игровой таймер бесконечный
    clock.tick(40)# частота обновления экрана
    pygame.display.update()# обновление содержимого экрана
    for event in pygame.event.get(): # прохождение по событиям
        if event.type==pygame.QUIT:#если нажать на крестик
            pygame.QUIT()# выход из игры