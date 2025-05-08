import pygame # type: ignore # PYRODIUS
import math
import random

clock = pygame.time.Clock()
score_value = 0
pygame.font.init() 
font = pygame.font.SysFont("Arial", 24)
overfont = pygame.font.SysFont("Arial", 84)


textX = 30
textY = 30

width = 960
height = 800
pygame.init()
display = pygame.display.set_mode((width,height))
pygame.display.set_caption("Pyrodius") 
icon = pygame.image.load("res/game.png")
pygame.display.set_icon(icon)

bgi = pygame.image.load("res/bg.png")
scroll = 0
tiles = math.ceil(width /bgi.get_width()) + 1

class Player:
    def __init__(self, playerSprite, playerX, playerY, playerX_change, playerY_change):
        self.playerSprite = playerSprite
        self.playerX = playerX
        self.playerY = playerY
        self.playerX_change = playerX_change
        self.playerY_change = playerY_change
    def playerDisplay(self, x,y): # player sprite display
        display.blit(self.playerSprite,(x,y))
    def get_rect(self):
        return self.playerSprite.get_rect(topleft=(self.playerX, self.playerY))

p1 = Player(pygame.image.load("res/player.png"), 170, 40, 0, 0)
p1.playerSprite = pygame.transform.scale(p1.playerSprite, (64, 64))

class Enemy:
    def __init__(self, enemySprite, enemyX, enemyY, enemyX_change):
        self.enemySprite = enemySprite
        self.enemyX = enemyX
        self.enemyY = enemyY
        self.enemyX_change = enemyX_change
    def enemyDisplay(self, x, y):
        display.blit(self.enemySprite, (x, y))
    def get_rect(self):
        return self.enemySprite.get_rect(topleft=(self.enemyX, self.enemyY))

enemy_sprites = [
    pygame.image.load("res/enemy.png"),
    pygame.image.load("res/enemy2.png"),
    pygame.image.load("res/enemy3.png"),
]

class Bullet:
    def __init__(self, bulletSprite, bulletX, bulletY, bulletX_change, bullet_state):
        self.bulletSprite = bulletSprite
        self.bulletX = bulletX
        self.bulletY = bulletY
        self.bulletX_change = bulletX_change
        self.bullet_state = bullet_state
    def bulletDisplay(self, x, y):
        self.bullet_state = "fire"
        display.blit(self.bulletSprite, (x, y))
    def get_rect(self):
        return self.bulletSprite.get_rect(topleft=(self.bulletX, self.bulletY))

bul = Bullet(pygame.image.load("res/bullet.png"), p1.playerX, p1.playerY, 20, "off")

def score (x,y): #score display
    score = font.render("Score: " + str(score_value), True, (255,255,255))
    display.blit(score, (x,y))

def bullet(x,y): # bullet -||-
    global bullet_state
    bul.bullet_state= "fire"
    display.blit(bulletSprite, (x+16,y+9))

def collision(rect1, rect2):
    return rect1.colliderect(rect2)

def game_over ():
    global scroll
    bul.bullet_state= "off"
    p1.playerX = 2000 #"clear
    enemy.enemyX = 2000
    scroll=0
    over = overfont.render("GAME OVER" , True, (255,255,255))
    display.blit(over, (350,300))

enemies = []
runtime = True
while runtime:
    clock.tick(50)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            runtime = False
        if event.type==pygame.KEYDOWN: #controls
            if event.key ==pygame.K_LEFT:
                p1.playerX_change = -4
            if event.key ==pygame.K_RIGHT:
                p1.playerX_change = 4
            if event.key ==pygame.K_UP:
                p1.playerY_change = -4
            if event.key ==pygame.K_DOWN:
                p1.playerY_change = 4
            if event.key ==pygame.K_SPACE:
                if bul.bullet_state == "off":
                    bul.bulletX = p1.playerX
                    bul.bulletY = p1.playerY
                    bul.bullet_state = "fire"
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key ==pygame.K_RIGHT:
                p1.playerX_change=0
            if event.key==pygame.K_DOWN or event.key ==pygame.K_UP:
                p1.playerY_change=0

    display.fill((0,0,0))
    display.blit(bgi, (0,0)) 
    i=0
    while(i<tiles):
        display.blit(bgi, (bgi.get_width()*i + scroll, 0))
        i+=1
  # FRAME FOR SCROLLING
    scroll -= 6

  # RESET THE SCROLL FRAME
    if abs(scroll) > bgi.get_width():
        scroll = 0
    p1.playerX += p1.playerX_change
    p1.playerY += p1.playerY_change

    if p1.playerX<0: #borders
        p1.playerX=0
    if p1.playerY<0:
        p1.playerY=0
    elif p1.playerY >636:
        p1.playerY=636

    if random.randint(0, 100) < 2:  # Adjust probability for enemy spawn rate
        enemy_type = random.choice(enemy_sprites)
        new_enemy = Enemy(enemy_type, 970, random.randint(0, height - 160), random.choice([-2, -3, -4]))
        enemies.append(new_enemy)

    for enemy in enemies[:]:
        enemy.enemyX += enemy.enemyX_change
        enemy.enemyDisplay(enemy.enemyX, enemy.enemyY)

    #if enemy.enemyX < 0:
        if enemy.enemyX < -enemy.enemySprite.get_width():
            enemies.remove(enemy)
            continue

        if collision(enemy.get_rect(), bul.get_rect()):
            bul.bullet_state = "off"
            bul.bulletX = p1.playerX  # Reset bullet to player position
            score_value += 100
            if enemy in enemies:
                enemies.remove(enemy)
            continue

        if enemy.enemyX>p1.playerX:
            enemy.enemyXchange=-3

        if collision(enemy.get_rect(), p1.get_rect()):
            game_over()

    if bul.bulletX>width:
        bul.bulletX= p1.playerX
        bul.bullet_state="off"
    if bul.bullet_state == "fire":
        bul.bulletDisplay(bul.bulletX, bul.bulletY)
        bul.bulletX+=bul.bulletX_change
    
    if score_value<=-100:
        game_over()

    p1.playerDisplay(p1.playerX, p1.playerY)

    score(textX, textY)
    pygame.display.update()
