from urllib.request import urlretrieve
import os

print("Please Turn off Lantern.\n\nPlease enter tile numbers.")
minx = int(input("minx: "))
maxx = int(input("maxx: "))
miny = int(input("miny: "))
maxy = int(input("maxy: "))
z = input("zoom level: ")

path = 'baidumaptiles'

if os.path.exists(path) is False:
    os.mkdir(path)

count = 0

for x in range(minx, maxx + 1):
    count += 1
    print(f'Downloading... {count}/{maxx-minx+1}', end='\r', flush=True)
    for y in range(maxy, miny - 1, -1):
        baidu_url = f'http://api0.map.bdimg.com/customimage/tile?&x={x}&y={y}&z={z}&udt=20171110&scale=1&ak=7x7kT5Qo9qBK5ucW6eqGF16qsToonADj&styles=t%3Abackground%7Ce%3Aall%7Cc%3A%23000000ff%7Ch%3A%23000000%2Ct%3Aroad%7Ce%3Aall%7Cc%3A%23ffffffff%7Ch%3A%23ffffff%2Ct%3Apoi%7Ce%3Aall%7Cv%3Aoff%2Ct%3Arailway%7Ce%3Aall%7Cv%3Aoff%2Ct%3Asubway%7Ce%3Aall%7Cv%3Aoff%2Ct%3Asubwaystation%7Ce%3Aall%7Cv%3Aoff%2Ct%3Aarterial%7Ce%3Al%7Cv%3Aoff%2Ct%3Abuilding%7Ce%3Aall%7Cv%3Aoff%2Ct%3Aroad%7Ce%3Al%7Cv%3Aoff%2Ct%3Amanmade%7Ce%3Al%7Cv%3Aoff'
        urlretrieve(baidu_url, f'{path}/x={x}&y={y}.jpeg')

print('\nDownload complete!')

os.system('pause')
