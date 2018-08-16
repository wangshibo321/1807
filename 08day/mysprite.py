import pygame
SCREEN_RECT = pygame.Rect(0,0,480,700)
class GameSprite(pygame.sprite.Sprite):#父类
	def __init__(self,imagename,speed=1):
		super().__init__() #调用父类方法
		self.image = pygame.image.load(imagename)
		self.rect = self.image.get_rect()
		self.speed = speed
	def update(self):
		self.rect.y+=self.speed
class EnemySprite(GameSprite):
	def __init__(self):
		self.imagename = "/home/laowang/1807/images/enemy0.png"
		super().__init__(self.imagename)

	def update(self):
		super().update()

class BackGroundSprite(GameSprite):
	def __init__(self,is_alt=False):
		self.imagename = "/home/laowang/1807/images/background.png"
		super().__init__(self.imagename,100)
		if is_alt:
			self.rect.y = - self.rect.height

	def update(self):
		super().update()
		if self.rect.top >= SCREEN_RECT.height:
			self.rect.y = - self.rect.height



