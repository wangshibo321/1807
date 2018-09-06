import pygame
from GameSprite import *

class PlanMain():

    def __init__(self):
        #创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        #创建游戏时钟
        self.clock = pygame.time.Clock()
        #调用精灵组
        self.__create_sprites()
        # 4. 设置定时器事件 - 每秒创建一架敌机
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)

        pygame.time.set_timer(CREATE_BULLET_EVENT, 500)

        # 创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()

        #敌机销毁精灵组
        self.enemy1_down_group = pygame.sprite.Group()

        self.count = 0

        self.score = 0 #分数

    def __create_sprites(self):
        '''创建精灵组'''
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1,bg2)#创建精灵组


        # 英雄组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)


    def start_game(self):
        pygame.init()

        """开始游戏"""
        print("开始游戏...")

        while True:
            self.count += 1

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

    def __event_handler(self):

        """事件监听"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                print("敌机出场...")
                enemy = Enemy()
                self.enemy_group.add(enemy)
                #讓英雄發射子彈
            elif event.type == CREATE_BULLET_EVENT:
                self.hero.fire()

         # 获取用户按键
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 6
            print('向右')
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -6
            print('向左')
        elif keys_pressed[pygame.K_UP]:
            self.hero.speed1 = -4
            print('向上')
        elif keys_pressed[pygame.K_DOWN]:
            self.hero.speed1 = 4
            print('向下')
        else:
            self.hero.speed1 = 0
            self.hero.speed = 0
            print('不移動')


    def __check_collide(self):
        """碰撞检测"""
        #子弹摧毁敌机
        #敌机精灵组在前，并返回敌机的精灵
        enemy_down = pygame.sprite.groupcollide(self.enemy_group,self.hero.bullet_group,True,True)

        enemy1_down_group.add(enemy_down)#加入到销毁组



        enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)

        if len(enemies) > 0:
            self.hero.kill()
            #结束游戏
            PlanMain.__game_over()

    def __update_sprites(self):
        """更新精灵组"""
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)
	#绘制分数
        self.drawText(str(self.score),SCREEN_RECT.width - 30,50)

        #敌机销毁
        for enemy1_down in enemy1_down_group:
            self.screen.blit(enemy1_down_surface[enemy1_down.down_index],enemy1_down.rect)
            if self.count % 15 == 0:
                enemy1_down.down_index += 1
                if enemy1_down.down_index == 3:
                    self.score +=5
                    enemy1_down_group.remove(enemy1_down)
                    print(self.score)

    @staticmethod

    def __game_over():
       """游戏结束"""
       print("游戏结束")
       pygame.quit()
       exit()

    def drawText(self,text,posx,posy,textHeight=48,fontColor=(0,0,0),backgroudColor=(255,255,255)):
        fontObj = pygame.font.Font(None, textHeight)  # 通过字体文件获得字体对象
        textSurfaceObj = fontObj.render(text, True,fontColor,backgroudColor)  # 配置要显示的文字
        textRectObj = textSurfaceObj.get_rect()  # 获得要显示的对象的rect
        textRectObj.center = (posx, posy)  # 设置显示对象的坐标
        self.screen.blit(textSurfaceObj, textRectObj)  # 绘制字

if __name__ == '__main__':
    planmain = PlanMain()
planmain.start_game()
