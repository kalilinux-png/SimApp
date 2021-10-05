import requests as req
import os
order_type=str(input('Enter B for Buy S for Sell-->').upper())
exchange=str(input('Enter the exchange N for nifty B for Bse-->').upper())
exchange_segement=str(input('Enter the exchange segment ex: C D U-->').upper())
scrip_code=int(input('Enter the scrip code ex 1660-->').upper())
quantity=int(input('Enter the quantity-->').upper())
price=int(input('Enter the price-->').upper())
is_intraday=True
atmarket=True

print(req.post(f"https://d7k2d7.deta.dev/place_order/{order_type}/{exchange}/{exchange_segement}/{scrip_code}/{quantity}/{price}/{is_intraday}/{atmarket}").text)
os.system('start python pnl.py ')

