import random
import pygame
SCREEN_RECT = pygame.Rect(0,0,480,700)
CREATE_ENEMY_EVENT = pygame.USEREVENT#常量
class GameSprite(pygame.sprite.Sprite):#父类
	def __init__(self,imagename,speed=1):
		super().__init__()#调用父类方法
		self.image = pygame.image.load(imagename)
		self.rect = self.image.get_rect()
		self.speed = speed

	def update(self):
		self.rect.y+=self.speed


class EnemySprite(GameSprite):#敌机子类		
	def __init__(self):
		self.imagename = "/home/laowang/1807/images/enemy0.png"
		super().__init__(self.imagename)
		self.rect.bottom = 0
		maxvalue = SCREEN_RECT.width-self.rect.width
		self.rect.x = random.randint(0,maxvalue)
		self.speed = random.randint(1,10)
		# self.speed = 50

	def update(self):
		super().update()
		if self.rect.top >= SCREEN_RECT.height:
			self.kill()


class BackGroundSprite(GameSprite):#背景精灵类
	def __init__(self,is_alt=False):
		self.imagename = "/home/laowang/1807/images/background.png"
		super().__init__(self.imagename,10)
		if is_alt:
			self.rect.y = - self.rect.height

	def update(self):
		super().update()
		if self.rect.top >= SCREEN_RECT.height:
			self.rect.y = - self.rect.height


class HeroSprite(GameSprite):#英雄 
	def __init__(self):
		self.imagename = "/home/laowang/1807/images/hero.gif"
		super().__init__(self.imagename,0)#0速度
		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.top = 550
		self.bullet_group = pygame.sprite.Group()


	def update(self):
		# super().update()
		self.rect.x+=self.speed	

		if self.rect.left <= 0:
			self.rect.left = 0

		if self.rect.right >= SCREEN_RECT.width:
			self.rect.right = SCREEN_RECT.width	

		self.rect.y+=self.speed1
		if self.rect.top <= 0:
			self.rect.top = 0

		if self.rect.bottom >= SCREEN_RECT.height:
			self.rect.bottom = SCREEN_RECT.height

	def fire(self):
		bullet = BulletSprite()
		bullet.rect.centerx = self.rect.centerx
		bullet.rect.y = self.rect.top - 20
		self.bullet_group.add(bullet)


		bullet1 = BulletSprite()
		bullet1.rect.centerx = self.rect.centerx - 35
		bullet1.rect.y = self.rect.top +35
		self.bullet_group.add(bullet1)

		bullet2 = BulletSprite()
		bullet2.rect.centerx = self.rect.centerx + 35
		bullet2.rect.y = self.rect.top + 35
		self.bullet_group.add(bullet2)


class BulletSprite(GameSprite):#子弹精灵
	def __init__(self):
		self.imagename = "/home/laowang/1807/images/bullet1.png"	
		super().__init__(self.imagename,-20)
	
	def __del__(self):
		print("子弹销毁了")	

	def update(self):
		super().update()
		if self.rect.bottom <= 0:
			self.kill()		


