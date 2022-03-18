import pygame 
import sys
import random
from pygame.mixer import Sound
from pygame import RLEACCEL
pygame.init()

def start_back_music():
    pygame.mixer.music.load("assets/Apoxode_-_Electric_1.mp3")
    pygame.mixer.music.play(loops=-1)
def stop_music():
    pygame.mixer.music.stop()
def load_sound(name):
    path = "assets/"+name
    return Sound(path)
class ne_scam():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000,500))
        pygame.display.set_caption("Windows заблокирована!!")
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.enemies = pygame.sprite.Group()
        self.cloud = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        self.ADDENEMY = pygame.USEREVENT+1
        pygame.time.set_timer(self.ADDENEMY,250)
        self.ADDCLOUD = pygame.USEREVENT+2
        pygame.time.set_timer(self.ADDCLOUD,1000)
        self.colision = load_sound("Collision.mp3")
        start_back_music()
    def draw(self):
        self.screen.fill((135,206,250))
        for entity in self.all_sprites:
            self.screen.blit(entity.surfing,entity.rect)
        pygame.display.flip()
        self.clock.tick(60)
    def game_logic(self):
        if self.player and pygame.sprite.spritecollide(self.player,self.enemies,False):
            self.player.kill()
            self.player = None
            self.colision.play()
            stop_music()
            pygame.time.delay(100)
            sys.exit()
        self.enemies.update()
        self.cloud.update()
    def main_loop(self):    
        while 1:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    sys.exit()
                if i.type == pygame.KEYDOWN:
                    if i.key == pygame.K_ESCAPE:
                        quit()
                if i.type == self.ADDENEMY:
                    new_enemy = Enemy()
                    self.enemies.add(new_enemy)
                    self.all_sprites.add(new_enemy)
                if i.type == self.ADDCLOUD:
                    new_cloud = Cloud()
                    self.cloud.add(new_cloud)
                    self.all_sprites.add(new_cloud)
            pressed_keys = pygame.key.get_pressed()
            if self.player:
                self.player.update(pressed_keys)
            self.game_logic()
            self.draw()
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()    
        self.surfing = pygame.image.load("assets/jet.png")   
        self.surfing.set_colorkey((255,255,255), RLEACCEL) 
        self.surfing = self.surfing.convert_alpha()
        self.rect = self.surfing.get_rect()
    def update(self,pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0,-5)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0,5)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5,0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5,0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 1000:
            self.rect.left = 1000
        if self.rect.top < 0: 
            self.rect.top = 0
        if self.rect.bottom > 500:
            self.rect.bottom = 500  
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy,self).__init__()
        self.surfing = pygame.image.load("assets/missile.png")   
        self.surfing.set_colorkey((255,255,255), RLEACCEL) 
        self.surfing = self.surfing.convert_alpha()
        self.rect = self.surfing.get_rect(center = (random.randint(1020,1100),random.randint(0,1000)))
        self.speed = random.randint(5,20)
    def update(self):
        self.rect.move_ip(-self.speed,0)
        if self.rect.right < 0:
            self.kill()
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud,self).__init__()
        self.surfing = pygame.image.load("assets/cloud.png")   
        self.surfing.set_colorkey((0,0,0), RLEACCEL) 
        self.surfing = self.surfing.convert_alpha()
        self.rect = self.surfing.get_rect(center = (random.randint(1020,1100),random.randint(0,1000)))
    def update(self):
        self.rect.move_ip(-5,0)
        if self.rect.right < 0:
            self.kill()
a = ne_scam()
a.main_loop()