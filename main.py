from PIL import Image, ImageDraw
import perlin_noise

canvas = Image.new("RGBA", size=(800, 800), color=(255, 255, 255, 255))
draw = ImageDraw.Draw(canvas)

def natural_line():
    pass

canvas.show()