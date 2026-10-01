# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 15:48:48 2025

@author: Solo
"""

#[0:planet index, 1:planet name, 2:mass, 3:radius, 4:init x, 5:init y,
# 6:init dx, 7:init dy, 8:color]

import pygame, math

def update_DxDy(planet_index):
    for i in range(len(planets_initState)):
        if i == planet_index:
            continue
        delta_x = planets_currState[i][4] - planets_currState[planet_index][4]
        delta_y = planets_currState[i][5] - planets_currState[planet_index][5]
        r = math.sqrt(delta_x ** 2 + delta_y ** 2)
        planets_currState[planet_index][6] +=\
            G*planets_initState[i][2]*delta_x/(r**3)
        planets_currState[planet_index][7] +=\
            G*planets_initState[i][2]*delta_y/(r**3)
        
def update_xy(planet_index):
    planets_currState[planet_index][4] += planets_currState[planet_index][6]
    planets_currState[planet_index][5] += planets_currState[planet_index][7]


class Planet(pygame.sprite.Sprite):
    def __init__(self, i, init_x, init_y, radius, color):
        pygame.sprite.Sprite.__init__(self)
        self.i=i
        self.image = pygame.Surface([radius*2, radius*2])
        pygame.draw.circle(self.image, color, (radius, radius), radius, 0)
        self.rect=self.image.get_rect()
        self.rect.center=(init_x, init_y)

    def update(self, i, x, y):
        if i == self.i:
            self.rect.center=(x, y)

"""main"""
planets_initState=[]
planet=[]

"""物體參數"""
#[0:planet index, 1:planet name, 2:mass, 3:radius, 4:init x, 5:init y,
# 6:init dx, 7:init dy, 8:color]
G=300
planets_initState.append([0, "name1", 100, 10, 20, 400, 5, 0, (0, 0, 255)])
planets_initState.append([1, "name2", 1, 10, 1100, 700, -2, -1, (255, 0, 0)])
planets_currState=planets_initState

pygame.init()
screen=pygame.display.set_mode((1200, 800))#視窗大小
pygame.display.set_caption("重力模型")#視窗標題
background=pygame.Surface(screen.get_size())
background=background.convert()
background.fill((0, 0, 0))
allsprite=pygame.sprite.Group()
for i in range(len(planets_initState)):
    planet.append(Planet(i, planets_initState[i][4], planets_initState[i][5],\
                       planets_initState[i][3], planets_initState[i][8]))
    allsprite.add(planet[i])

"""主迴圈"""
clock = pygame.time.Clock()
running=True
while running:
    clock.tick(30)#每秒30幀
    screen.blit(background, (0,0))
    for event in pygame.event.get():#check視窗是否被關閉
        if event.type == pygame.QUIT:
            running = False
    
    for i in range(len(planets_initState)):
        update_DxDy(i)
        print(planets_currState[i])
    for i in range(len(planets_initState)):
        update_xy(i)
        print(planets_currState[i])
    print()
    for i in range(len(planets_initState)):
        planet[i].update(i, planets_currState[i][4], planets_currState[i][5])
    allsprite.draw(screen)
    pygame.display.update()
pygame.quit()

