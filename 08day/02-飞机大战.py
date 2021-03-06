import pygame
from mysprite import *
class PlaneGame(object):
	def __init__(self):
		self.screen = pygame.display.set_mode(SCREEN_RECT.size)
		self.clock = pygame.time.Clock()
		self.__create_sprites()
	def start_game(self):
		while True:
			#1.设置刷新频率
			self.clock.tick(60)
			#2.事件监听
			self.__event_handler()
			#3.碰撞检测
			self.__check_collide()
			#4.更新精灵组
			self.__update_sprites()
			#5.更新屏幕显示
			pygame.display.update()
	def __create_sprites(self):#创建精灵组和精灵组
		bg1 = BackGroundSprite()
		bg2 = BackGroundSprite(True)
		self.bg_group = pygame.sprite.Group(bg1,bg2)

	def	__event_handler(self):
		"""事件监听"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				PlaneGame.__game_over()
	def __check_collide(self):
		"""碰撞检测"""
		pass
	def __update_sprites(self):
		"""更新精灵组"""
		self.bg_group.update()
		self.bg_group.draw(self.screen)


	@staticmethod
	def __game_over():
		"""游戏结束"""
		print("游戏结束")
		pygame.quit()
		exit()
if __name__ == "__main__":
	#创建游戏对象
	game = PlaneGame()
	#开始游戏
	game.start_game()
