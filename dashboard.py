import pygame
import time
import requests as req
import random
from menu import order_section
from pygame.locals import *
import os

class dashboard():

    

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Profit and Loss')
        font_name, font_size = 'inconsolata', 32
        self.font = pygame.font.SysFont(font_name, font_size)
        self.color_fg, self.color_bg = pygame.Color(0xfff31bff), pygame.Color(0x1e2320ff)
        self.screen=pygame.display.set_mode((1080,700))
        self.screen.fill(pygame.Color(0x1e2320ff))
        pygame.display.flip()
        self.watchlist=[ ]

    def add_watchlist(self,item=[ ]):
        self.watchlist.append(item)

    


    def pnl_script(self):
        print('inside pnl script')
        s2=pygame.Surface((400,900))
        # s2.fill(self.color_bg)
        s2.fill(self.color_bg)
        row=0
        last_order=int(req.get('https://d7k2d7.deta.dev/len').text)+1
        print('len of orders',last_order)
        for k in range(1,last_order):
            print('inside for loop')
        # for k in range(1,100):
            for event in pygame.event.get():
                if event.type == QUIT:
                    print('quit form 42')
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    print('RANDOM KEY PRESSED')
                    if event.key == pygame.K_SPACE:
                        print('f1 pressed')
                        order_section()
            scrip_pnl=req.get(f'https://d7k2d7.deta.dev/script/pnl/{k}').text
            # scrip_pnl=k
            print(k,'scrip_pnl',scrip_pnl)
            pandl_script_text=self.font.render(str(scrip_pnl),True,self.color_fg)
            s2.blit(pandl_script_text,[0,row])
            self.screen.blit(s2,[0,0])
            self.flip()
            row+=17
                


    def live_pnl(self):
        live_pnl_scrn=pygame.Surface((300,50))
        live_pnl_scrn.fill(self.color_bg)
        # self.screen.blit(live_pnl_scrn,[500,0])
        # self.flip()
        pandl=0
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    print('key down from 71')
                    if event.key == K_SPACE:
                        print('space pressed on live pnl')
                        order_section()
            pandl=req.get('https://d7k2d7.deta.dev/pnl').text
            print('got pnl',pandl)
            text=self.font.render(f"LIVE PNL "+str(pandl),True,(0,255,0))
            live_pnl_scrn.blit(text,[0,0])
            self.screen.blit(live_pnl_scrn,[500,0])
            self.flip()
            live_pnl_scrn.fill(self.color_bg)
            # pandl+=1
            self.pnl_script()



    def flip(self):
        pygame.display.flip()


    

if __name__=='__main__':
    d=dashboard()
   
    # d.pnl_script()
    d.live_pnl()
    print('done live pnl')

    


















































# class dashboard():
#     pygame.init()
#     screen = pygame.display.set_mode((500, 500))
#     pygame.display.set_caption('Profit and Loss')
#     font = pygame.font.Font(None, 50)
#     screen.fill((80, 80, 80))
#     watchlist=pygame.draw.rect(screen,(255,255,255),(0,0,400,600))
# # add_button=pygame.draw.rect(screen,(255,255,255))
# def take():
#     return  player_name.get()

# def watchlist():
#     player_name.pack(pady=30)
#     Button(
#         root,
#         text="Add to Watchlist",
#         padx=10,
#         command=take,
#         pady=5,
        
#         ).pack()

#     root.mainloop()









    
# def add_to_watch():
#     while True:
#         for k in pygame.event.get():
#             if k.type==QUIT:
#                 print('quit')
#                 pygame.quit()
#             if k.type==KEYDOWN:
#                 if k.key==pygame.K_BACKSPACE:
#                     print('backspace')
#                 if k.key == pygame.K_a:
#                     print('a is pressed')
#                     watchlist()
                    
                    
        



# def add_text(text='Hello world', loc=[150, 150], color=(255, 255, 255), screen=screen):
#     text = str(text)
#     text = font.render(text, True, color)
#     screen.blit(text, loc)
#     pygame.display.flip()
#     print('flip')
    


# if __name__ == '__main__':
#     add_to_watch()
#     # add_text()
#     # add_text('watchlist',loc=[0,0],color=(150,200,150))
#     # time.sleep(2)
#     # pygame.quit()
