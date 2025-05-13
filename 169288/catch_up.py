from pygame import *
import game2
import lose
import pygame
fps = time.Clock()

screen = display.set_mode((1000,700))
display.set_caption('Minecraft')
background = transform.scale(image.load('fon.jpg'),(1000, 700))

mixer.init()  
mixer.music.load('mine.mp3')
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
        if keybord[K_d] and self.rect.x < 875:
            self.rect.x += 10
            self.image = self.r_img
        screen.blit(self.image, (self.rect.x, self.rect.y))
hero = Hero('steave.png',3, 0, 1)
diamond = Hero('diamond.jpg', 850, 0, 0)


class Enemy(GameEnemy):
    def enemy_move(self):
        if self.rect.x > 890:
            self.move = 'left'

        if self.rect.x < 0:
            self.move = 'right'

        if self.move == "right":
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed
    def enemy_move_up(self):
        if self.rect.y > 450:
            self.move_up = 'up'

        if self.rect.y < 0:
            self.move_up = 'down'

        if self.move_up == "down":
            self.rect.y += self.speed
        else:
            self.rect.y -= self.speed
mish = Enemy("mish.png", 850, 150, 15)
mish2 = Enemy("mish.png", 0, 450, 15)



class Wall(sprite.Sprite):
    def __init__(self, x, y, w, h, r, g, b):
        super().__init__()
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.r = r
        self.g = g
        self.b = b

        self.main_wall = Surface((self.w, self.h))
        self.main_wall.fill((r,g,b))
        self.rect_wall = self.main_wall.get_rect()
        self.rect_wall.x = self.x
        self.rect_wall.y = self.y
    
    def show_wall(self):
        screen.blit(self.main_wall, self.rect_wall)

w1 = Wall(160,0,10,540,124, 252, 0)
w2 = Wall(320,160,10,540,124, 252, 0)
w3 = Wall(480,0,10,540,124, 252, 0)
w4 = Wall(640,160,10,540,124, 252, 0)
w5 = Wall(800,0,10,540,124, 252, 0)


hp = 3
images =[]
for i in range(1,5):
    images.append(transform.scale(image.load(f"{i}.png"), (70, 30)))
run = True
while run:
    for i in event.get():
        if i.type == QUIT:
            run = False
        elif hero.rect.colliderect(diamond.rect):
            game2.start_game()
            run = False
    screen.blit(background, (0,0))

    diamond.reset()
    hero.move_hero()
    w1.show_wall()
    w2.show_wall()
    w3.show_wall()
    w4.show_wall()
    w5.show_wall()
    mish.reseting()
    mish.enemy_move()
    mish2.reseting()
    mish2.enemy_move()
    


    if hero.rect.colliderect(w1.rect_wall):
        kick.play()
        hero.rect. x = 3
        hero.rect. y = 0
        hp -= 1
    if hero.rect.colliderect(w2.rect_wall):
        kick.play()
        hero.rect. x = 3
        hero.rect. y = 0
        hp -= 1
    if hero.rect.colliderect(w3.rect_wall):
        kick.play()
        hero.rect. x = 3
        hero.rect. y = 0
        hp -= 1
    if hero.rect.colliderect(w4.rect_wall):
        kick.play()
        hero.rect. x = 3
        hero.rect. y = 0
        hp -= 1
    if hero.rect.colliderect(w5.rect_wall):
        kick.play()
        hero.rect. x = 3
        hero.rect. y = 0
        hp -= 1
    if hero.rect.colliderect(mish.rect):
        kick.play()
        hero.rect. x = 3
        hero.rect. y = 0
        hp -= 1
    if hero.rect.colliderect(mish2.rect):
        kick.play()
        hero.rect. x = 3
        hero.rect. y = 0
        hp -= 1



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
