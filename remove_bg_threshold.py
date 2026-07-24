from PIL import Image

def process():
    img = Image.open('anatomy_bg.png').convert('RGBA')
    pixels = img.load()
    width, height = img.size
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            if a < 40:
                pixels[x, y] = (0, 0, 0, 0)
    img.save('anatomy_bg.png')
    print("Noise threshold applied.")

if __name__ == "__main__":
    process()
