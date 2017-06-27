def write_on_image():
    from PIL import Image
    from PIL import ImageFont
    from PIL import ImageDraw
    img = Image.open("back.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Aaargh.ttf", 16)
    draw.text((10, 10), "Hey, This is sample text - kapeed2091", (200, 200, 100), font=font)
    img.save('back-out.jpg')
    return
