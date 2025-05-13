from pygame import *
import pygame
import time

def lose():
    clock = pygame.time.Clock()
    pygame.init()

    mixer.init()  
    mixer.music.load('loser.mp3')
    mixer.music.play()

    screen = display.set_mode((1000,700))
    display.set_caption('Minecraft')
    background = transform.scale(image.load('open.jpg'),(1000, 700))

    font = pygame.font.Font(None, 60)  
    text = font.render("Для закрытия, тыкните по экрану", True, (207, 0, 0))  
    text_rect = text.get_rect(center=(500, 600))  


      
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN:  # Кнопка закрытия или клик мыши
                running = False
        screen.blit(background, (0,0))
        if pygame.time.get_ticks() % 1000 < 500:
            screen.blit(text, text_rect)
        display.update()
        clock.tick(60) 