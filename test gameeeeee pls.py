import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("test game")

hodidqsno = [pygame.image.load('right 1.png'), pygame.image.load('right 2.png'), pygame.image.load('right 3.png'), pygame.image.load('right 4.png'), pygame.image.load('right 5.png'), pygame.image.load('right 6.png'), pygame.image.load('right 7.png'), pygame.image.load('right 8.png'), pygame.image.load('right 9.png')]
hodilqvo = [pygame.image.load('left 1.png'), pygame.image.load('left 2.png'), pygame.image.load('left 3.png'), pygame.image.load('left 4.png'), pygame.image.load('left 5.png'), pygame.image.load('left 6.png'), pygame.image.load('left 7.png'), pygame.image.load('left 8.png'), pygame.image.load('left 9.png')]
backg = pygame.image.load('bg.jpg')
nemurda = pygame.image.load('front 1.png')

chasovnic = pygame.time.Clock()

x = 50
y = 425
width = 64
height = 64
vel = 5

lqvo = False
dqsnp = False

isJump = False
jumpCount = 10

krachkobroqch = 0

win.blit(backg, (0, 0))

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.lqvo = False
        self.dqsnp = False
        self.krachkobroqch = 0
        self.jumpCount = 10

    def draw(self, win):
        if self.krachkobroqch + 1 >= 27:
            self.krachkobroqch = 0

        if self.lqvo:
            win.blit(hodilqvo[self.krachkobroqch//3], (self.x,self.y))
            self.krachkobroqch += 1
        elif self.dqsnp:
            win.blit(hodidqsno[self.krachkobroqch//3], (self.x,self.y))
            self.krachkobroqch +=1
        else:
            win.blit(nemurda, (self.x,self.y))


def redrawGameWindow():
    win.blit(backg, (0,0))
    chovek.draw(win)
    pygame.display.update()

#loop
chovek = player(300, 410, 64, 64)
run = True
while run:
    chasovnic.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and chovek.x > chovek.vel:
        chovek.x -= chovek.vel
        chovek.lqvo = True
        chovek.dqsnp = False
    elif keys[pygame.K_RIGHT] and chovek.x< 500 - chovek.width - chovek.vel:
        chovek.x += chovek.vel
        chovek.dqsnp = True
        chovek.lqvo = False
    else:
        chovek.dqsnp = False
        chovek.lqvo = False
        chovek.krachkobroqch = 0

    if not(chovek.isJump):
        if keys[pygame.K_SPACE]:
            chovek.isJump = True
            chovek.dqsnp = False
            chovek.lqvo = False
            chovek.krachkobroqch = 0
    else:
        if chovek.jumpCount >= -10:
            neg = 1
            if chovek.jumpCount < 0:
                neg = -1
            chovek.y -= (chovek.jumpCount ** 2) * 0.5 * neg
            chovek.jumpCount -= 1
        else:
            chovek.isJump = False
            chovek.jumpCount = 10

    redrawGameWindow()

pygame.quit()