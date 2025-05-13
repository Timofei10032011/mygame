from pygame import *
import time  as t
import win
import pygame
import lose
import pygame


def start_games():


    screen = display.set_mode((1000,700))
    display.set_caption('Minecraft')
    background = transform.scale(image.load('mir.jpg'),(1000, 700))
    fps = time.Clock()

    mixer.init()
    mixer.music.load('key-m.mp3')
    mixer.music.play()

    kick = mixer.Sound('990.mp3')

    class GameSprite(sprite.Sprite):
        def __init__(self, player_image, player_x, player_y, player_sped):
            super().__init__()
            self.image = transform.scale(image.load(player_image), (100,130))

            self.l_img = transform.flip(self.image,True,False)
            self.r_img = self.image

            self.speed = player_sped
            self.rect = self.image.get_rect()
            self.rect.x = player_x
            self.rect.y = player_y
            self.move = "left" 
            self.move_up = 'up'
        def reset(self):
            screen.blit(self.image, (self.rect.x, self.rect.y))

    class Hero(GameSprite):
        def move_hero(self):
            keybord = key.get_pressed()
            if keybord[K_w] and self.rect.y > -1:
                self.rect.y -=10
            if keybord[K_s] and self.rect.y < 570:
                self.rect.y +=10
            if keybord[K_a] and self.rect.x > 4:
                self.rect.x -= 10
                self.image = self.l_img
            if keybord[K_d] and self.rect.x < 890:
                self.rect.x += 10
                self.image = self.r_img
            screen.blit(self.image, (self.rect.x, self.rect.y))

    hero = Hero('steave.png', 3, 300, 1)

    


    class GameEnemy(sprite.Sprite):
        def __init__(self, player_image, player_x, player_y, player_sped):
            super().__init__()
            self.image = transform.scale(image.load(player_image), (120,80))

            self.speed = player_sped
            self.rect = self.image.get_rect()
            self.rect.x = player_x
            self.rect.y = player_y
            self.move = "left" 
            self.move_up = 'up'
        def reseting(self):
            screen.blit(self.image, (self.rect.x, self.rect.y))

    class GameEnemyCase(sprite.Sprite):
        def __init__(self, player_image, player_x, player_y, player_sped):
            super().__init__()
            self.image = transform.scale(image.load(player_image), (100,100))

            self.speed = player_sped
            self.rect = self.image.get_rect()
            self.rect.x = player_x
            self.rect.y = player_y
            self.move = "left" 
            self.move_up = 'up'
        def case(self):
            screen.blit(self.image, (self.rect.x, self.rect.y))
    

    class Enemy(GameEnemy):
        def enemy_move(self):
            if mish.rect.x < hero.rect.x:
                mish.rect.x += speed
            if mish.rect.x > hero.rect.x:
                mish.rect.x -= speed
            if mish.rect.y < hero.rect.y:
                mish.rect.y += speed
            if mish.rect.y > hero.rect.y:
                mish.rect.y -= speed
        def enemy_move_2(self):
            if mish2.rect.x < hero.rect.x:
                mish2.rect.x += speed2
            if mish2.rect.x > hero.rect.x:
                mish2.rect.x -= speed2
            if mish2.rect.y < hero.rect.y:
                mish2.rect.y += speed2
            if mish2.rect.y > hero.rect.y:
                mish2.rect.y -= speed2
        def enemy_move_3(self):
            if mish3.rect.x < hero.rect.x:
                mish3.rect.x += speed3
            if mish3.rect.x > hero.rect.x:
                mish3.rect.x -= speed3
            if mish3.rect.y < hero.rect.y:
                mish3.rect.y += speed3
            if mish3.rect.y > hero.rect.y:
                mish3.rect.y -= speed3
       


    
    mish = Enemy("dragons.png", 770, 0, 15)
    mish2 = Enemy("dragons.png", 770, 600, 15)
    mish3 = Enemy("dragons.png", 770, 300, 15)

    

    diamond = GameEnemyCase('case.png', 850, 300, 0)
    
    speed = 2
    speed2 = 4
    speed3 = 3

    hp = 3
    images =[]
    for i in range(1,5):
        images.append(transform.scale(image.load(f"{i}.png"), (70, 30)))
    run3 = True
    while run3:
        for i in event.get():
            if i.type == QUIT:
                run3 = False
            if hero.rect.colliderect(diamond.rect):
                pygame.quit()
                win.win()

        screen.blit(background, (0,0))
        mish.reseting()
        mish.enemy_move()
        mish2.reseting()
        mish2.enemy_move_2()
        mish3.reseting()
        mish.enemy_move_3()

        
        
       
       
        diamond.case()

        
    
        hero.move_hero()
       
        if hero.rect.colliderect(mish.rect):
            kick.play()
            hero.rect. x = 3
            hero.rect. y = 300
            hp -= 1
            mish.rect. x = 770
            mish.rect. y = 0
            mish2.rect. x = 770
            mish2.rect. y = 600
            mish3.rect. x = 770
            mish3.rect. y = 300


        if hero.rect.colliderect(mish2.rect):
            kick.play()
            hero.rect. x = 3
            hero.rect. y = 300
            hp -= 1
            mish.rect. x = 770
            mish.rect. y = 0
            mish2.rect. x = 770
            mish2.rect. y = 600
            mish3.rect. x = 770
            mish3.rect. y = 300


        if hero.rect.colliderect(mish3.rect):
            kick.play()
            hero.rect. x = 3
            hero.rect. y = 300
            hp -= 1
            mish.rect. x = 770
            mish.rect. y = 0
            mish2.rect. x = 770
            mish2.rect. y = 600
            mish3.rect. x = 770
            mish3.rect. y = 300



        if hp == 3:
            screen.blit(images[0], (6,10))
        elif hp == 2:
            screen.blit(images[1], (6,10))
        elif hp == 1:
            screen.blit(images[2], (6,10))
        elif hp == 0:
            pygame.quit()
            lose.lose()
            


        display.update()
        fps.tick(60) 






