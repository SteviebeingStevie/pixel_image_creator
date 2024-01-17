from PIL import Image
import random

canvas_size = (100, 100)
canvas = Image.new('RGB', canvas_size, color='white')
px = canvas.load()



for x in range(100):
    for y in range(100):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)



        px[(x), (y)] = [r,g,b]





canvas.show()

"""



im.show()


loaded_image = Image.open("images/before/proxy-image.jpeg")
print(loaded_image.size)
"""