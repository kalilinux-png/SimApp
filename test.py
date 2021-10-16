import requests as req
print(req.get("https://d7k2d7.deta.dev/time").text)
print(req.post("https://d7k2d7.deta.dev/place_order/B/N/C/3456/1/200/true/true").text)
print(req.post("https://d7k2d7.deta.dev/place_order/B/N/C/3456/1/100/true/true").text)
print(req.get("https://d7k2d7.deta.dev/position").text)
# print(req.post("http://127.0.0.1:8000/place_order/B/N/C/3456/1/500/true/true").text)
# print(req.post("http://127.0.0.1:8000/place_order/B/N/C/3456/1/500/true/true").text)

print(req.get("https://d7k2d7.deta.dev/status/1").text)
