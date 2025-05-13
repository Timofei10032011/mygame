from pygame import *
def win():
    fps = time.Clock()

    mixer.init()  
    mixer.music.load('game-won.mp3')
    mixer.music.play()

    screen = display.set_mode((1000,700))
    display.set_caption('Minecraft')
    background = transform.scale(image.load('win.png'),(1000, 700))

    run = True
    while run:
        for i in event.get():
            if i.type == QUIT:
                run = False
        screen.blit(background, (0,0))
        display.update()
        fps.tick(60) 