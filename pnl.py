import pygame
import time
import requests as req
import os
def main():
    pygame.init()
    screen=pygame.display.set_mode((250,250))
    pygame.display.set_caption('Profit and Loss')
    font=pygame.font.Font(None,30)
    frame=60
    screen.fill((255,255,255))
    ''' To get the live pnl uncomment the below line and del the sco from everywhere and make chn in line 23'''
    # pnl=req.get('https://d7k2d7.deta.dev/pnl').text
    # sco=0
    while True:
        screen.fill((255,255,255))
        for k in pygame.event.get():
            if k.type==pygame.QUIT:
                pygame.quit()
        # sco=str(sco)
        pnl=req.get('https://d7k2d7.deta.dev/pnl').text
        PNL='LIVE PNL'
        pnl=font.render(pnl,True,(0,0,0))
        PNL=font.render(PNL,True,(50,50,50))
        screen.blit(pnl,[100,5])
        screen.blit(PNL,[5,5])
        # for k in range(100):
        a=req.get('https://d7k2d7.deta.dev/script/pnl').text
        print(a)
        # a=[[str(k) for k in range(f) ] for f in range(10)]
        # a=[['a','b','c','d'],['e','f','g','h'],['i','j','k','l'],['m','n','o','p']]
        for k in range(len(a)):
            print(k*30+100)
            print(' '.join(a[k]))
            string=font.render(' '.join(a[k]),True,(0,0,0))
            screen.blit(string,[0,k*30+100])
            pygame.display.flip()
        # sco=int(sco)+1
        pygame.display.flip()

if __name__=='__main__':
    main()
