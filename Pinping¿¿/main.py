from pygame import *

# pygame setup
init()
screen = display.set_mode((700, 500))
display.set_caption('Ping-pong')
clock = time.Clock()
running = True


class GameSprite(sprite.Sprite):
    def __init__(self, imagen, x, y, velocidad, scale):
        super().__init__()
        self.image = transform.scale(image.load(imagen), scale)
        self.velocidad = velocidad
        self.velocidady = velocidad
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def dibujar(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def movimiento(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >= 0:
            self.rect.y -= self.velocidad
        if keys[K_s] and self.rect.y <= 499:
            self.rect.y += self.velocidad
    def movimiento2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >= 0:
            self.rect.y -= self.velocidad
        if keys[K_DOWN] and self.rect.y <= 499:
            self.rect.y += self.velocidad
    def set_image(self):
        self.image = self.images[self.damage]

class Ball(GameSprite):
    def movimiento(self):
        self.rect.x += self.velocidad
        self.rect.y += self.velocidady
        if self.rect.y <= 0 or self.rect.y >= 480:
            self.velocidady *= -1


barra1 = Player(r'C:\Users\Vic\Documents\Pinping¿¿\racket.png', 15, 350, 5, (25, 135))
barra2 = Player(r'C:\Users\Vic\Documents\Pinping¿¿\racket.png', 635, 350, 5, (25, 135))
ball = Ball(r'C:\Users\Vic\Documents\Pinping¿¿\tenis_ball.png', 350, 250, 5, (20, 20))



while running:
    for vent in event.get():
        if vent.type == QUIT:
            running = False
    screen.fill((29, 107, 63))
    barra1.dibujar()
    barra2.dibujar()
    ball.dibujar()
    barra1.movimiento()
    barra2.movimiento2()
    ball.movimiento()
    if sprite.collide_rect(barra1, ball) or sprite.collide_rect(barra2, ball):
        ball.velocidad *= -1
    if ball.rect.x <= 0 or ball.rect.x >= 680:
        ball.rect.x = 350
        ball.rect.y = 250

    # flip() the display to put your work on screen
    display.update()

    clock.tick(60)  # limits FPS to 60

quit()
