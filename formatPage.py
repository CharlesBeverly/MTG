from PIL import Image, ImageOps
import os
import math

def createPage(cards):

    width = 672
    height = 936

    # Combine the images vertically
    widthCorrection = 139 + 15
    heightCorrection = 71 + 15
    
    index = 0
    imagecounter = 1
    while(index < len(cards)):
        combined_image = Image.new("RGB", (width * 3, height * 3), (255,255,255, 0))

        for x in range(3):
            if index == len(cards):
                break
            for y in range(3):
                if index == len(cards):
                    break
                image = Image.open("cards/" + cards[index][1] + ".png")
                index += 1
                combined_image.paste(image, (width*x, height*y))
        
        combined_image.save("test.png")

        padding = (widthCorrection, heightCorrection, widthCorrection, heightCorrection)
        combined_image = ImageOps.expand(combined_image, padding, fill = (255,255,255, 0))
        combined_image = combined_image.convert("L")
        # Save the combined image
        combined_image.save("output/image"+(str)(imagecounter)+".png")
        imagecounter+=1