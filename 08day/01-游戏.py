import pygame
from mysprite import *
pygame.init()
screen = pygame.display.set_mode((480,700))
bg = pygame.image.load("/home/laowang/1807/images/background.png")
#screen.blit(bg,(0,0))

hero = pygame.image.load("/home/laowang/1807/images/hero1.png")
#screen.blit(hero,(200,500))
herorect = pygame.Rect(200,500,120,120)
clock = pygame.time.Clock()#创建游戏时钟

enemy = EnemySprite()#创建敌机精灵
enemy1 = EnemySprite()#创建敌机精灵
enemy1.rect.x = 50
enemy1.speed = 2
enemy2 = EnemySprite()
enemy2.rect.x = 250
enemy2.speed = 1
enemy_group = pygame.sprite.Group(enemy,enemy1,enemy2)

	





while True:
	clock.tick(60)#一秒刷新60次
	herorect.y -= 1 #相当于速度
	screen.blit(bg,(0,0))
	screen.blit(hero,herorect)
	if herorect.bottom <= 0:#控制飞机返航
		herorect.top = 700
	enemy_group.update()#更新
	enemy_group.draw(screen)#画到哪



	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print("退出游戏")
			pygame.quit()
			exit()





	pygame.display.update()#更新

pygame.init()


