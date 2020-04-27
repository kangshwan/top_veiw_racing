import os
import pygame as pg
import random
from setting import *
from time import sleep
import math

vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    
    def __init__(self, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.walking = False
        self.current_frame = 0
        self.lase_update = 0
        self.load_images()
        #self.image = self.standing_frames[0]
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.acc_max = vec()

    def load_images(self):
        self.image = pg.Surface((32, 32))
        self.image.fill(BLACK)
        self.arm_image = pg.Surface((32,64))
        self.arm_image.fill(LIGHTBLUE)
        pass

    def update(self):
        self.animate()
        self.acc = vec(0,0)
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_d]:
           
            self.acc.x = PLAYER_ACC
        if keys[pg.K_w]:
            self.acc.y = -PLAYER_ACC
        if keys[pg.K_s]:
            self.acc.y = PLAYER_ACC
        
        # apply friction
        self.acc += self.vel*PLAYER_FRICTION
        #equations of motion
        print('magnitude:', math.sqrt(self.vel.x**2+self.vel.y**2))
        print(self.vel)
        print('accelate:',self.acc)
        self.vel = self.vel + 0.3*self.acc
        if math.sqrt(self.vel.x**2+self.vel.y**2) >3:
            self.vel *= 3/math.sqrt(self.vel.x**2+self.vel.y**2)
        self.pos += self.vel
        self.rect.midbottom = self.pos
    def animate(self):
        pass
    def magnitude(self):
        return
