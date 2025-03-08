import pygame as pistrun

pistrun.init()  # обязательная каманда people
window_size = (300, 300)  # dont
screen = pistrun.display.set_mode(window_size)  # создание экрана(окна) с размера 300x300 (можно в него выйти?)
pistrun.display.set_caption("БАСУХА В ДЕЛЕ РОДНЫЕ")  # название окна
backgound_color = (255, 255, 255)  # цвет
clock = pistrun.time.Clock()  # создание игровово таймера

pistrun.display.update()

height = 50
width = 50
height = 150
x = 150
y = 150
r = pistrun.Rect(x, y, width, height)

while True:  # игрововй таймер
    clock.tick(40)  # частота обновления таймераааааа
    pistrun.draw.rect(screen, (0, 0, 255), r)
    pistrun.draw.circle(screen, (0, 255, 0), (x, y), radius=27)
    pistrun.display.update()  # обновление содержимого экрана
    screen.fill(backgound_color)  # заполнение окна цветоm
    for event in pistrun.event.get():  # проходимся по событиям
        if event.type == pistrun.QUIT:  # если нажали на крестик
            pistrun.QUIT()  # выйти из ГОЙДА
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit();
                        sys.exit("И Я СТОЮ В ПОЛ ОБОРОТА")
        if event.type == pistrun.KEYDOWN:
            if event.key == pistrun.K_a:
                r.x -= 10
            elif event.key == pistrun.K_d:
                r.x += 10
            elif event.key == pistrun.K_w:
                r.y -= 10
            elif event.key == pistrun.K_s:
                r.y += 10
        if event.type == pistrun.KEYDOWN:
            if event.key == pistrun.K_LEFT:
                x -= 10
            elif event.key == pistrun.K_RIGHT:
                x += 10
            elif event.key == pistrun.K_UP:
                y -= 10
            elif event.key == pistrun.K_DOWN:
                y += 10
    if x >= 327:
        x = -27
        print("А В ШУМНОМ ЗАЛЕ РЕСТОРАНА!!!!!!")
