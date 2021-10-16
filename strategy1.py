import requests as req
from menu import Model
from strategy_back import get_hl
from tkinter import messagebox
import os 
from tkinter import *
# https://d7k2d7.deta.dev/ltp/N/C/1660
url = "https://d7k2d7.deta.dev/ltp/"
exch='N'
exch_seg='C'
token=1660

def mess(text='None',title='None'):
    messagebox.showinfo(title=title,message=text)
# print(req.get(url+f"{exch}/{exch_seg}/{token}").text)

def taker():
    root=Tk()
    root.title('Strategy 1')
    m=Model(root,'Strategy1')
    exch = m.label(text='Exchange',row=0,column=0) ; exch_ent = m.Ent(row=0,column=1)
    stock_name = m.label(text='Stock Code',row=1,column=0) ; stock_name_ent = m.Ent(row=1,column=1)
    exch_type = m.label(text='Exchange Type',row=2,column=0) ; exch_type_ent = m.Ent(row=2,column=1)
    t1 = m.label(text='Start from',row=3,column=0) ; t1_ent = m.Ent(row=3,column=1) ; m.label(text='Hint --> 2021-month-date hour-min ',row=3,column=2)
    t2 = m.label(text='End to ',row=4,column=0) ; t2_ent = m.Ent(row=4,column=1)
    def throw_it():
        ans=[exch_ent.get(),exch_type_ent.get(),stock_name_ent.get(),t1_ent.get(),t2_ent.get()]
        # /history/{Exchange}/{Exchange_Type}/{Scrip_Code}/{'1m'}/{From_Data}/{To_Date}
        get_hl(ans)
        print('/'.join(ans))
        ans=get_hl('/'.join(ans),stock_name_ent.get()) 
        mess(text='\n'.join(ans))
    Button=m.button(text='Start Strategy',row=5,column=0,command=throw_it)
    m.active()
if __name__=='__main__':
    taker()