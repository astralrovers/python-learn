from PIL import Image

im = Image.open(r'.\picture\wm.png')
print(im.mode)
im.close()