import pygame
from mysprite import *
class PlaneGame(object):
	def __init__(self):
		self.screen = pygame.display.set_mode(SCREEN_RECT.size)
		self.clock = pygame.time.Clock()
		self.__create_sprites()

		pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)#定时事件
		#pygame.time.set_timer(CREATE_BULLET_ECENT,500)
		self.enemy_group = pygame.sprite.Group()
		self.enemy1_down_group = pygame.sprite.Group()
		self.count = 0
		self.score = 0

	def start_game(self):
		while True:
			self.count+=1
			# 1. 设置刷新帧率
			self.clock.tick(60)
			# 2. 事件监听
			self.__event_handler()
			# 3. 碰撞检测
			self.__check_collide()
			# 4. 更新精灵组
			self.__update_sprites()
			# 5. 更新屏幕显示
			pygame.display.update()

	def __create_sprites(self):#创建精灵组和精灵组
		bg1 = BackGroundSprite()
		bg2 = BackGroundSprite(True)
		self.bg_group = pygame.sprite.Group(bg1,bg2)
		self.enemy_group = pygame.sprite.Group()#创建敌机精灵组

		self.hero = HeroSprite()
		self.hero_group = pygame.sprite.Group(self.hero)
		
		
		

    	        
	def __event_handler(self):
		"""事件监听"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				PlaneGame.__game_over()
			elif event.type == CREATE_ENEMY_EVENT:
				self.enemy_group.add(EnemySprite())
				#print("事件被触发了")

				enemy = EnemySprite()
				self.enemy_group.add(enemy)#通过add方法添加
				#self.hero.fire()自动发射
		#获取用户按键
		keys_pressed = pygame.key.get_pressed()

		if keys_pressed[pygame.K_RIGHT]:
			self.hero.speed = 10
		elif keys_pressed[pygame.K_LEFT]:
			self.hero.speed = -10
		elif keys_pressed[pygame.K_UP]:
			self.hero.speed1 = -10
		elif keys_pressed[pygame.K_DOWN]:
			self.hero.speed1 = 10
		else:
			self.hero.speed = 0
			self.hero.speed1 = 0
		if keys_pressed[pygame.K_SPACE]:
			print("该发射子弹了")
			self.hero.fire()	


	def __check_collide(self):
		"""碰撞检测"""

		
		#子弹摧毁敌机
		enemy_down = pygame.sprite.groupcollide(self.enemy_group,self.enemy_group,True,True)
		#敌机撞毁英雄
		#enemy1_down_group.add(enemy_down)
		enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
		#判断列表时候有内容
		if len(enemies) > 0:
			#让英雄牺牲
			self.hero.kill()
			#结束游戏
			PlaneGame.__game_over()
	
	def __update_sprites(self):
		"""更新精灵组"""
		self.bg_group.update()
		self.bg_group.draw(self.screen)
		

		self.enemy_group.update()
		self.enemy_group.draw(self.screen)

		self.hero_group.update()
		self.hero_group.draw(self.screen)

		self.hero.bullet_group.update()
		self.hero.bullet_group.draw(self.screen)

	@staticmethod
	def __game_over():
	   """游戏结束"""

	   print("游戏结束")
	   pygame.quit()
	   exit()	

	def drawText(self,test,posx,posy,textHeight=48,fontColor=(0,0,0),backgroudColor=(255,255,255)):
		fontObj = pygame.font.Font(None,textHeight)
		textSurfaceObj = fontObj.render(text,True,fontColor,backgroudColor)
		textRectObj = textSurfaceObj.get_rect()
		textRectObj.center = (posx,posy)
		self.screen.blit(textSurfaceObj,textRectObj)

if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()

    # 开始游戏
    game.start_game()



