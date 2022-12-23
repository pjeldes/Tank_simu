import pygame as pg
import json
__ORANGE__ = [255, 140, 0]
__BLACK__ = [0, 0, 0]
__WHITE__ = [255, 255, 255]
__GREEN__ = [0, 255, 0]


class Watter:
    def __init__(self) -> None:
        self.heigth = 5
        self.min_heigth = 5
        self.speed = 1
        self.max_heigth = 235
        self.content = pg.Rect(190, 175, 235, 235)
        self.content_empytied = pg.Rect(190, 175, 235, 235)
    def put_in_screen(self, screen):
        pg.draw.rect(screen, __ORANGE__, self.content)
        pg.draw.rect(screen, __BLACK__, self.content_empytied)

    def increase_level(self):
        count = float(self.content_empytied.height)
        count -= float(self.speed)
        print("count: " + str(count))
        self.content_empytied.height = int(count)
    def scale_dimension_tank(self, real_hight):
        hight = float(real_hight/self.max_heigth)*self.heigth
        hight = round(hight, 2)
        return hight


    def decrease_level(self):
        count = float(self.content_empytied.height)
        count += self.speed
        print("count: " + str(count))
        self.content_empytied.height = int(count)
        #self.content_empytied.height += self.speed


class Main:
    def __init__(self) -> None:
        self.runing = True
        self.screen_width = 500
        self.screen_height = 800
        self.background = pg.image.load("img/Tank_simu.jpg")

        #screen
        self.screen = pg.display.set_mode((self.screen_width, self.screen_height))
        pg.display.set_caption("Simulacion Estanque")

        ## make watter
        content_tank = Watter()

        ## font
        self.font = pg.font.Font('freesansbold.ttf', 20)

        while self.runing:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.runing = False
            self.screen.blit(self.background, (0,0))
            ## LOGICAL ##
            pressed_key = pg.key.get_pressed()
            if pressed_key[pg.K_UP]:
                if content_tank.content_empytied.height > 0:
                    content_tank.increase_level()
                    #real height
                    content_tank.heigth = 235 - content_tank.content_empytied.height
                    print(content_tank.heigth)
            if pressed_key[pg.K_DOWN]:
                if content_tank.content_empytied.height  < 235:
                    content_tank.decrease_level()
                    content_tank.heigth = 235 - content_tank.content_empytied.height
                    print(content_tank.heigth)

            ## END LOGICAL ##
            self.alarma_text = self.font.render("{}[m]".format(content_tank.scale_dimension_tank(4)), True, __BLACK__, None)
            self.screen.blit(self.alarma_text, (385, 45))
            content_tank.put_in_screen(self.screen)
            pg.display.flip()
if __name__ == "__main__":
    pg.init()
    App = Main()