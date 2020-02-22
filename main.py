import sys
import pygame
from pygame.locals import *

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Paddle:
    def __init__(self, image, num, speed):
        self.image = image
        self.speed = speed
        self.pos = image.get_rect().move(num * 550 + 20, 150)
    def move(self, w, h):
        self.pos = self.pos.move(w * self.speed, h * self.speed)
        if self.pos.top < 0:
            self.pos.top = 0
        if self.pos.bottom > 400:
            self.pos.bottom = 400

class Ball:
    def __init__(self, image, speed):
        self.image = image
        self.speed = speed
        self.pos = image.get_rect().move(286, 187)
        self.direction = Vector2(1, 1)
    def move(self):
        self.pos = self.pos.move(self.direction.x * self.speed, self.direction.y * self.speed)
        if self.pos.bottom > 400 or self.pos.top < 0:
            self.direction.y = -self.direction.y
pygame.init()
size = width, height = 600, 400
black = 0, 0, 0

paddle1 = Paddle(pygame.image.load("paddle.png"), 0, 5)
paddle2 = Paddle(pygame.image.load("paddle.png"), 1, 5)
ball = Ball(pygame.image.load("ball.png"), 3)

screen = pygame.display.set_mode(size)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    keys=pygame.key.get_pressed()
    if keys[K_w]:
        paddle1.move(0, -1)
    if keys[K_s]:
        paddle1.move(0, 1)
    if keys[K_UP]:
        paddle2.move(0, -1)
    if keys[K_DOWN]:
        paddle2.move(0, 1)

    ball.move()

    screen.fill(black)
    screen.blit(paddle1.image, paddle1.pos)
    screen.blit(paddle2.image, paddle2.pos)
    screen.blit(ball.image, ball.pos)
    pygame.time.delay(int(1 / 30 * 1000))
    pygame.display.flip()