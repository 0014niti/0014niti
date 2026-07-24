from PIL import Image

def process():
    img = Image.open('anatomy_bg.png').convert('RGBA')
    pixels = img.load()
    width, height = img.size
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            brightness = max(r, g, b)
            if brightness > 0:
                nr = min(255, int(r * 255 / brightness))
                ng = min(255, int(g * 255 / brightness))
                nb = min(255, int(b * 255 / brightness))
                pixels[x, y] = (nr, ng, nb, brightness)
            else:
                pixels[x, y] = (0, 0, 0, 0)
    img.save('anatomy_bg.png')
    print("Background removed successfully.")

if __name__ == "__main__":
    process()
