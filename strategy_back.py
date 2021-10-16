import requests as req
from tkinter import messagebox
mess=''
def get_hl(data):
    url=f"https://d7k2d7.deta.dev/hl/"+'/'.join(data)
    print(url)
    ans=req.get(url).json()
    high,low=ans['high'],ans['low']
    print(high,low)
    while True:
        ltp=float(req.get(f"https://d7k2d7.deta.dev/ltp/{data[0]}/{data[1]}/{data[2]}").json())
        
        # make sure you get the high low in some kind of good form so that you can extract data easily
        if high > ltp > low:
            print("In Range")
        else:
            print('range break info ')
            
            mess=f'Upper Range Break High {high} Low {low } Ltp {ltp}' if ltp > high else  f'Lower Range Break  {high} Low {low } Ltp {ltp}'
            if high > ltp :
                action = "B"
            else:
                action = "S"
            
            mess+=req.post(f"https://d7k2d7.deta.dev/place_order/{action}/{data[0]}/{data[1]}/{data[2]}/{1}/{-1}/true/true").text
            

            messagebox.showinfo(message=mess)
            break
