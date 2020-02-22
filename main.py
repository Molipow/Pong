import sys
import pygame
from pygame.locals import *

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, x, y):
        self.x = self.x + x
        self.y = self.y + y

class Paddle:
    def __init__(self, image, num, speed):
        self.image = image
        self.num = num
        self.speed = speed
        self.pos = Vector2(num * 550 + 20, 150)
        self.width = 10
        self.height = 100
    def move(self, w, h):
        self.pos.move(w * self.speed, h * self.speed)
        if self.pos.y + self.height > 400:
            self.pos.y = 400 - self.height
        if self.pos.y < 0:
            self.pos.y = 0

class Ball:
    def __init__(self, image, speed):
        self.image = image
        self.speed = speed
        self.pos = Vector2(287, 187)
        self.width = 25
        self.height = 25
        self.direction = Vector2(1, 1)
    def move(self):
        self.pos.move(self.direction.x * self.speed, self.direction.y * self.speed)
        if self.pos.y + self.height > 400 or self.pos.y < 0:
            self.direction.y = -self.direction.y
    def detect_collision(self, _paddle):
        if (_paddle.num == 1 and self.pos.x + self.width > _paddle.pos.x and self.pos.y + self.height > _paddle.pos.y and self.pos.y < _paddle.pos.y + _paddle.height) or (_paddle.num == 0 and self.pos.x < _paddle.pos.x + _paddle.width and self.pos.y + self.height > _paddle.pos.y and self.pos.y < _paddle.pos.y + _paddle.height):
            self.direction.x = -self.direction.x
            # self.direction.y = _paddle.height/2
    def check_for_win(self):
        global score1, score2
        if self.pos.x <= 0:
            score2 += 1
            reset()
        if self.pos.x + self.width >= 600:
            score1 += 1
            reset() 

def reset():
    ball.pos = Vector2(287, 187)
    ball.direction = Vector2(1, 1)
    paddle1.pos = Vector2(20, 150)
    paddle2.pos = Vector2(570, 150)

pygame.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
score1, score2 = 0, 0
size = width, height = 600, 400
black = 0, 0, 0


paddle1 = Paddle(pygame.image.load("paddle.png"), 0, 5)
paddle2 = Paddle(pygame.image.load("paddle.png"), 1, 5)
ball = Ball(pygame.image.load("ball.png"), 7)

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
    ball.detect_collision(paddle1)
    ball.detect_collision(paddle2)
    ball.check_for_win()

    scoretext = myfont.render(f'{score1}:{score2}', False, (255, 255, 255))

    screen.fill(black)
    screen.blit(scoretext,(286,100))
    screen.blit(paddle1.image, (paddle1.pos.x, paddle1.pos.y))
    screen.blit(paddle2.image, (paddle2.pos.x, paddle2.pos.y))
    screen.blit(ball.image, (ball.pos.x, ball.pos.y))
    pygame.time.delay(int(1 / 30 * 1000))
    pygame.display.flip()