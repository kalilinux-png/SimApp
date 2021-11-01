import pygame
from menu import watchlist
from tkinter import *
import threading
import time
from pygame.version import ver
import requests as req
import random
from menu import order_section
from strategy1 import taker
from pygame.locals import *
from menu import option_menu
import os


class dashboard():

    def __init__(self):
        pygame.init()
        self.color_pur=(222,129,240)
        self.color_back=(52,63,86)
        pygame.display.set_caption('Profit and Loss')
        font_name, font_size = 'inconsolata', 32
        self.font = pygame.font.SysFont(font_name, font_size)
        self.color_fg, self.color_bg = pygame.Color(
            0xfff31bff), pygame.Color(0x1e2320ff)
        
        self.screen = pygame.display.set_mode((1080, 700))
        # self.screen.fill(pygame.Color(0x1e2320ff))
        self.screen.fill(self.color_back)
        self.watch_list_screen=pygame.Surface((400,800))
        self.watch_list_screen.fill(self.color_bg)
        pygame.display.flip()

    def watchlist(self):
        self.watch_list_screen.blit(self.font.render("WATCHLIST",True,(0,255,0)),[0,0])
        ans=req.get("https://d7k2d7.deta.dev/watchlist").json()
        print('here is the ans from line 31',ans)
        for k in range(len(ans)):
            text=map(str,ans[k])
            print('hey bro',text)
            watch = self.font.render(
                ' '.join(text), True,self.color_pur)
            self.watch_list_screen.blit(watch, [0, k*30+50])
            self.screen.blit(self.watch_list_screen,[800,0])
            self.flip()
        

    def events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                print('quit form 42')
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print('space pressed')
                    order_section()
                if event.key == pygame.K_s:
                    print('hey some key is pressed might be s')
                    taker()
                if event.key == pygame.K_w:
                    print('watchlist button')
                    watchlist()
                if event.key == pygame.K_o:
                    print('option menu')
                    option_menu()
    def pnl_script(self):
        print('inside pnl script')
        s2 = pygame.Surface((400, 900))
        # s2.fill(self.color_bg)
        s2.fill(self.color_bg)
        row = 0
        last_order = int(req.get('https://d7k2d7.deta.dev/len').text)+1
        print('len of orders', last_order)
        for k in range(1, last_order):
            print('inside for loop')
        # for k in range(1,100):
            self.events()
            scrip_pnl = req.get(f'https://d7k2d7.deta.dev/script/pnl/{k}').text
            # scrip_pnl=k
            print(k, 'scrip_pnl', scrip_pnl)
            pandl_script_text = self.font.render(
                str(scrip_pnl), True, self.color_fg)
            s2.blit(pandl_script_text, [0, row])
            self.screen.blit(s2, [0, 0])
            self.flip()
            row += 17


    def live_pnl(self):
        live_pnl_scrn = pygame.Surface((300, 50))
        live_pnl_scrn.fill(self.color_bg)
        # self.screen.blit(live_pnl_scrn,[500,0])
        # self.flip()
        pandl = 0
        while True:
            self.events()
            pandl = req.get('https://d7k2d7.deta.dev/pnl').text
            print('got pnl', pandl)
            text = self.font.render(f"LIVE PNL "+str(pandl), True, (0, 255, 0))
            live_pnl_scrn.blit(text, [0, 0])
            self.screen.blit(live_pnl_scrn, [500, 0])
            self.flip()
            live_pnl_scrn.fill(self.color_bg)
            # pandl+=1            
            self.pnl_script()

    def flip(self):
        pygame.display.flip()


if __name__ == '__main__':
    d = dashboard()
    d.live_pnl()


    # d.pnl_script()
    # d.live_pnl()
    # print('done live pnl')

