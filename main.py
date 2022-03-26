from PIL import Image, ImageDraw, ImageFont

# https://we.tl/t-EBleZvmhqQ
def _generate_image(baseimage, name, outfolder, contentext):

    image = Image.open(baseimage)
    width, height = image.size

    draw = ImageDraw.Draw(image)
    text = contentext
    textwidth, textheight = draw.textsize(text)
    font = ImageFont.truetype('DejaVuSerif.ttf', 24)

    margin = 100
    _x = width - textwidth-margin
    _y = height-textheight - margin

    draw.text((_x, _y), text, (0, 0, 0), font)
    image.save(f'{outfolder}/{name}', optimize=True, quality=50)


LIMIT = 101
for x in range(1, LIMIT):
    _generate_image('sample.jpg', f'{x}.jpg', 'out', f'Page {x}/{LIMIT-1}')
