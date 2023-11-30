from PIL import Image
import imagineer



mandel = Image.effect_mandelbrot((3840, 2160), (-2.0, -1.2, 1.0, 1.2), 500)

mandel.show()
mandel.save("images/after/Bild2.jpg")

