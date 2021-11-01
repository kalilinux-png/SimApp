print('start')
from tkinter import *
import requests as req
from tkinter import messagebox

root=Tk()
print('root')
root.title('Hello')


options = req.get("http://127.0.0.1:8000/options/strategy").json()

print('new',options)

for k in options.values():
    try:

        print(k['exchange'],k['ltp'])

        if k['ltp'] >= k['B']  or  k['ltp'] <= k['S'] :
            if k['ltp'] >= k['B'] :
                messagebox.showinfo(title='Alert',message=f"Buy {k['scrip_code']}")
            elif k['ltp'] <= k['S'] :
                messagebox.showinfo(title='Alert',message=f"sell {k['scrip_code']}")
            # print(req.post
            print(f"http://127.0.0.1:8000/update/options/{k['scrip_code']}") # .text)

    except Exception as e:
        print(e)
  
    


   

