from tkinter import *
import os
import requests as req
from tkinter import messagebox
# root=Tk(screenName='Main Menu')
# root.title('Main Menu App')


class Model():

    def __init__(self, root, title):
        self.title = title
        self.root = root

    def Ent(self, text='Entery', row=0, column=0):
        ent = Entry(self.root)
        ent.grid(row=row, column=column)
        return ent

    def label(self, text='Label', row=0, column=0):
        # Header=Label(self.root,text='Welcome to the family of Omi Pvt Ltd...')
        # Header.grid(row=row,column=column)

        label = Label(self.root, text=text)
        label.grid(row=row, column=column)
        return label

    def button(self, text='Button', row=0, column=0, command=None):
        but = Button(self.root, text=text, command=command)
        but.grid(row=row, column=column)
        return but

    def active(self):
        self.root.title = self.title
        self.root.mainloop()


def order_section():
    root = Tk()
    root.title = 'Orders'
    m = Model(root, 'Place Order')
    exch = m.label(text='Exchange =>', row=1, column=0)
    exch_ent = m.Ent(text='ent', row=1, column=1)  # ent for exch

    exch_segment = m.label(text='Exchange Segment =>', row=2, column=0)
    exch_segment_ent = m.Ent(text='ent', row=2, column=1)  # ent for segment

    token = m.label(text='token =>', row=3, column=0)
    token_ent = m.Ent(text='ent', row=3, column=1)  # ent for token

    quantity = m.label(text='quantity =>', row=5, column=0)
    quantity_ent = m.Ent(text='ent', row=5, column=1)  # ent for token

    action = m.label(text='Buy/Sell =>', row=4, column=0)
    action_ent = m.Ent(text='ent', row=4, column=1)  # ent for action

    price = m.label(text='Price=>', row=6, column=0)
    price_ent = m.Ent(text='ent', row=6, column=1)  # ent for action

    def sender():
        entries = [action_ent.get(), exch_ent.get(), exch_segment_ent.get(
        ), token_ent.get(), quantity_ent.get(), price_ent.get(),'true','true']
        url = "https://d7k2d7.deta.dev/place_order/"+'/'.join(entries)
        print(url)
        response=req.post(url).text
        messagebox.showinfo(title='Order Report',message=response)
    def pnl():
        os.system('python dashboard.py')
        # from dashboard import dashboard
        # d=dashboard()
        # d.live_pnl()
        

    but = m.button(text='Place Order',row=7, command=lambda: sender())
    but = m.button(text='Profit and loss',row=7,column=1, command=lambda:pnl())
    m.active()


if __name__ == '__main__':
    import time
    order_section()
