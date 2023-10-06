# імпортуємо бібліотеки
from pygame import *
init()
# задаємо розмір екрану
W = 700
H = 700
# створюємо вікно
window = display.set_mode((W, H))
display.set_caption("Labyrinth")
display.set_icon(image.load("treasure.png"))
 
back = transform.scale(image.load("background.jpg"), (W, H)) # вписує картинку у вікно
clock = time.Clock() # лічильник кадрів
# підключаємо музику
# mixer.init()
# mixer.music.load('jungles.ogg')
# mixer.music.play()
# mixer.music.set_volume(0.7)

kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')
# створюємо базовий клас з купою функцій
class GameSprite(sprite.Sprite):
    def __init__(self, player_img, player_x, player_y, speed):
        super().__init__() # викликаємо конструктор супер-класу
        self.image = transform.scale(image.load(player_img), (65, 65)) # створюємо картинку
        self.rect = self.image.get_rect() # повертає прямокутник під картинкою
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = speed
# метод для відображення картинки
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# клас з купою функцій
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < H - 65:
            self.rect.y += self.speed

        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < W - 65:
            self.rect.x += self.speed
# створюємо клас з купою функцій
class Enemy(GameSprite):
    direction = "right"

    def update(self, start, end):
        if self.rect.x >= end:
            self.direction = "left"
            self.image = transform.scale(image.load('cyborg_l.png'), (65, 65))
        if self.rect.x <= start:
            self.direction = "right"

        if self.direction == 'left':
            self.rect.x -= self.speed
        if self.direction == 'right':
            self.rect.x += self.speed
            self.image = transform.scale(image.load('cyborg.png'), (65, 65))

class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, wall_w, wall_h, wall_x, wall_y):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.width = wall_w
        self.height = wall_h
        self.image = Surface((self.width, self.height))
        self.image.fill((self.color1, self.color2, self.color3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
enemy1 = Enemy('cyborg.png', 300, 300, 2)
hero = Player('hero.png', 20, 20, 4)
gold = GameSprite('treasure.png', 550, 550, 0)
# створюємо стіни
wall1 = Wall(10, 100, 10, 200, 20, 20, 0)
wall2 = Wall(10, 100, 10, 20, 200, 220, 0)
wall3 = Wall(10, 100, 10, 300, 20, 220, 200)
wall4 = Wall(10, 100, 10, 20, 260, 500, 200)
wall5 = Wall(10, 100, 10, 20, 200, 80, 140)
wall6 = Wall(10, 100, 10, 200, 20, 80, 340)
wall7 = Wall(10, 100, 10, 20, 340, 280, 340)
wall8 = Wall(10, 100, 10, 200, 20, 500, 440)
# ігровий цикл
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(back, (0, 0))
    gold.reset()
    hero.reset()
    enemy1.reset()
    enemy1.update(300, 400)
    hero.update()
    gold.reset()
    wall1.reset()
    wall2.reset()
    wall3.reset()
    wall4.reset()
    wall5.reset()
    wall6.reset()
    wall7.reset()
    wall8.reset()
    # wall8.reset()
    clock.tick(30)
    display.update()
    if sprite.collide_rect(hero, wall1) or (sprite.collide_rect(hero, wall2)) or sprite.collide_rect(hero, wall3) or sprite.collide_rect(hero, wall4) or sprite.collide_rect(hero, wall5) or sprite.collide_rect(hero, wall6) or sprite.collide_rect(hero, wall7) or sprite.collide_rect(hero, enemy1):
        hero.rect.x = 40
        hero.rect.y = 20
    if sprite.collide_rect(hero, gold):
        game = False
