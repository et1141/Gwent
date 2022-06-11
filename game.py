import pygame,sys
#from playsound import playsound
from pygame import mixer

class Init_game(object):


    def __init__ (self):
        #******************config
        self.menu_width = 1280
        self.menu_height = 720
        self.rgb_config = (0, 150, 255)  # nasycenie czerwonego,zielonego, niebieskiego
        self.rgb_black = (0, 0, 0)  # black color
        self.rgb_white = (255, 255, 255)
        self.font_name = "fonts/2459-font.ttf"  # Got this font from fontsiland.com : https://fontsisland.com/font/gwent-extrabold
        #********************

        pygame.init()
        self.menu_window = pygame.display.set_mode((self.menu_width,self.menu_height))  # argument to podajemy to tupple, czyli para argumentow (szerokosc i wysokosc)
        self.START_KEY, self.BACK_KEY,  self.UP_KEY, self.DOWN_KEY = False, False, False, False
        self.gameOn = True
        #playsound(r'GaunterTheme.mpga',gameOn)
        pygame.mixer.init()
        pygame.mixer.music.load('music/GaunterTheme.mpga')
        pygame.mixer.music.play(-1)
        self.game_loop()



    def get_events(self):
        for event in pygame.event.get():  # przychwytujemy zdarzenia
           if event.type == pygame.QUIT:
                    self.gameOn = False
                    sys.exit(0)
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                    self.gameOn = False
                    sys.exit(0) ##
               if event.key == pygame.K_RETURN: #enter
                    self.START_KEY = True
               if event.key == pygame.K_BACKSPACE:
                   self.BACK_KEY = True
               if event.key == pygame.K_UP:
                   self.UP_KEY = True
               if event.key == pygame.K_DOWN:
                   self.DOWN_KEY = True
    def reset_events(self):
        self.START_KEY, self.BACK_KEY, self.UP_KEY, self.DOWN_KEY = False, False, False, False

    def game_loop(self):
        while True:
            self.get_events()
            self.menu_window.fill(self.rgb_black) #czyszczenie
            self.draw_text('Gwent',144,self.menu_width/2,self.menu_height/5,(255,0,0))
            # podwojne booforowanie: bloki rysuja sie nie na oknie tylko na innej klatce i odpowiednia komenda mozemy wyswietlic ta druga klatke
            pygame.display.flip()  # wyswietlenie ukrytej kartki
    def draw_text(self,text,size,x,y,color):
        font = pygame.font.Font(self.font_name,size)
        text_render = font.render(text,True,color)
        text_box = text_render.get_rect()
        text_box.center = (x,y)
        self.menu_window.blit(text_render,text_box)

