from PIL import Image, ImageFilter, ImageOps
import sys
import os

x = os.system("cls")
del x


def sharpen_wallpaper(image_folder, store_location):
    count = 0
    for filename in os.listdir(image_folder):
        count += 1
        wallpapers = Image.open(f'{image_folder}/{filename}')
        print(f'{count}.) {filename} is being Converted -->>', end=' ')
        rgb2xyz = (
            0.4552773, 0.3675500, 0.1413926, 0,
            0.3216999, 0.7032549, 0.3750452, 0,
            0.1139322, 0.0971045, 0.7141733, 0)
        out = wallpapers.convert("RGB", rgb2xyz)
        out = out.filter(ImageFilter.SHARPEN)
        ImageOps.solarize(out, 100)
        out.thumbnail((1920, 1080))
        name = os.path.splitext(filename)
        print(f'Stored As {store_location}/{name[0]}.png \n')
        out.save(f'{store_location}/{name[0]}-converted.png', "png")


try:
    if len(sys.argv) > 1:
        image_location = sys.argv[1]
        new_location = sys.argv[2]

    else:
        image_location = str(input("Enter File Name: "))
        new_location = str(input("Enter Store Location: "))
    if os.path.exists(image_location):
        if not os.path.exists(new_location):
            os.system(f'mkdir {new_location}')
        sharpen_wallpaper(image_location, new_location)
        print("Success !!")
    else:
        print("Path Doesn't Exist")
except FileNotFoundError:
    print("File Not Found !!!! Unsuccessful! ")
    exit(0)
finally:
    print("======= PROGRAM ENDS ========")
