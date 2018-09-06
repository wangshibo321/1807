import random
import pygame

SCREEN_RECT = pygame.Rect(0,0,480,700)
#刷新帧率
FRAME_PER_SEC = 60
#敌机事件的常量
CREATE_ENEMY_EVENT = pygame.USEREVENT

#子弹事件常量
CREATE_BULLET_EVENT = pygame.USEREVENT + 1

#爆炸销毁图片
bg1 = pygame.image.load('/home/laowang/1807/images/enemy0_down1.png')
bg2 = pygame.image.load('/home/laowang/1807/images/enemy0_down2.png')
bg3 = pygame.image.load('/home/laowang/1807/images/enemy0_down3.png')
bg4= pygame.image.load('/home/laowang/1807/images/enemy0_down4.png')

#爆炸的精灵组
enemy1_down_group = pygame.sprite.Group()

#把爆炸图片放到列表中
enemy1_down_surface = []
enemy1_down_surface.append(bg1)
enemy1_down_surface.append(bg2)
enemy1_down_surface.append(bg3)
enemy1_down_surface.append(bg4)


class GameSprite(pygame.sprite.Sprite):
	def __init__(self,image_name,speed=1):
		super().__init__()
		self.image = pygame.image.load(image_name)
		self.rect = self.image.get_rect()
		self.speed = speed

	def update(self):
		self.rect.y += self.speed	




class Background(GameSprite):

	def __init__(self,is_alt=False):
		image_name = "/home/laowang/1807/images/background.png"
		super().__init__(image_name)
		if is_alt:
			self.rect.y = -self.rect.height

	
	def update(self):
		super().update()
		if self.rect.y > SCREEN_RECT.height:
			self.rect.y = -self.rect.height




#1、随机x值 一定要有最大值 随机数
#2、初始化速度  随机1-?
#3、初始化y的位置
#敌人精灵
class Enemy(GameSprite):
	def __init__(self):
		image_name = "/home/laowang/1807/images/enemy-1.gif"
		super().__init__(image_name)
		self.speed  = random.randint(1,3)

		max_x = SCREEN_RECT.width - self.rect.width
		self.rect.x = random.randint(0,max_x)#随机位置

		self.rect.bottom = 0

		self.down_index = 0 #敌机销毁图片索引

	def update(self):
		super().update()
			
		if self.rect.y >= SCREEN_RECT.height:
			self.kill()

	def __del__(self):
		pass

class Hero(GameSprite):
	def __init__(self):
		image_name = "/home/laowang/1807/images/hero.gif"
		super().__init__(image_name,0)
		self.speed1 = 0

		self.rect.centerx = SCREEN_RECT.centerx	
		self.rect.bottom = SCREEN_RECT.bottom - 120
		
		#子弹精灵族	

		self.bullet_group = pygame.sprite.Group()
	def update(self):
		self.rect.x += self.speed
		self.rect.y += self.speed1


		if self.rect.left < 0:
			self.rect.left = 0

		if self.rect.right > SCREEN_RECT.width:
			self.rect.right = SCREEN_RECT.width	


		

	def fire(self):
		bullet = Bullet()#子弹精灵组
		bullet.rect.bottom = self.rect.y - 0
		bullet.rect.centerx = self.rect.centerx

		# 3. 将精灵添加到精灵组
		self.bullet_group.add(bullet)

		bullet1 = Bullet()
		bullet1.rect.bottom = self.rect.y + 0
		bullet1.rect.centerx = self.rect.centerx -35
		self.bullet_group.add(bullet1)

		bullet2 = Bullet()
		bullet2.rect.bottom = self.rect.y + 0
		bullet2.rect.centerx = self.rect.centerx + 35
		self.bullet_group.add(bullet2)

#创建子弹精灵

class Bullet(GameSprite):

	def __init__(self):
		image_name = "/home/laowang/1807/images/bullet1.png"
		super().__init__(image_name,-50)


	def update(self):
		super().update()
		if self.rect.bottom < 0:
			self.kill()

class Soruce(pygame.sprite.Sprite):

	def __init__(self):
		super().__init__()
		


	def update(self):
		super().update()
		if self.rect.bottom < 0:
			self.kill()



