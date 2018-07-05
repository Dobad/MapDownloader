from PIL import Image
import numpy as np
import os

print("Please enter tile numbers.")
minx = int(input("minx: "))
maxx = int(input("maxx: "))
miny = int(input("miny: "))
maxy = int(input("maxy: "))
outputfilename = input("output file's name: ")

path = 'stitchedbdtiles'

print('Horizontal stitching in process...', flush=True)

if os.path.exists(path) is False:
    os.mkdir(path)

count = 0

for y in range(maxy, miny-1, -1):
    count += 1
    print(f'stitching {count}/{maxy-miny+1}', end='\r', flush=True)
    list_im = []
    for x in range(minx, maxx+1):
        list_im.append(f'baidumaptiles/x={x}&y={y}.jpeg')
    imgs = [Image.open(i) for i in list_im]
    imgs_comb = np.hstack((np.asarray(i) for i in imgs))
    imgs_comb = Image.fromarray(imgs_comb)
    imgs_comb.save(f'stitchedbdtiles/y={y}.jpeg')

print('Complete!', flush=True)
print('Virtical stitching in process...', flush=True)

list_im = []
for y in range(maxy, miny-1, -1):
    list_im.append(f'stitchedbdtiles/y={y}.jpeg')
imgs = [Image.open(i) for i in list_im]
imgs_comb = np.vstack((np.asarray(i) for i in imgs))
imgs_comb = Image.fromarray(imgs_comb)
imgs_comb.save(f'{outputfilename}.jpeg')

print('Complete!')
print('All stitching process complete. Please check the current folder for the new jpeg file.')

os.system('pause')
