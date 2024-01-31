# Day 96
# AsyncIO in python
# asyncio is used for requesring or retrieving multiple data from server or form web at the same time.
# it is like you are puting 10 downloads at a time and it is downloading all parallely or concurrently.
import time
import asyncio 
import requests


async def function1():
  print("func 1") 
  URL = "https://wallpaperaccess.in/public/uploads/preview/1920x1200-desktop-background-ultra-hd-wallpaper-wiki-desktop-wallpaper-4k-.jpg"
  response = requests.get(URL)
#   time.sleep(2)
  open("wallpaper.jpg", "wb").write(response.content)
  return "Aakash"
  
async def function2():
  print("func 2") 
  URL = "https://p4.wallpaperbetter.com/wallpaper/490/433/199/nature-2560x1440-tree-snow-wallpaper-preview.jpg"
  response = requests.get(URL)
#   time.sleep(3)
  open("wallpaper1.jpg", "wb").write(response.content)
  
async def function3():
  print("func 3")
  URL = "https://c4.wallpaperflare.com/wallpaper/622/676/943/3d-hd-wikipedia-3d-wallpaper-preview.jpg"
  response = requests.get(URL)
#   time.sleep(4)
  open("wallpaper2.jpg", "wb").write(response.content)

async def main():
#   below function will execute one at a time 

  # await function1()
  # await function2()
  # await function3()
  # return 3

#   below function will execute all at once parallely
  L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
  print(L)
# insted of doing this you can just use gather() function
  # task = asyncio.create_task(function1())
  # # await function1()
  # await function2()
  # await function3()

asyncio.run(main())