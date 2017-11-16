#resizing without pixelate

from PIL import Image
large_size = (1920, 1200)

im = Image.open("yourImageHere") #your image here

image_w, image_h = im.size
aspect_ratio = image_w / float(image_h)
new_height = int(large_size[0] / aspect_ratio)      #getting the new height

#setting new width

if new_height < 1200:
    final_width = large_size[0]
    final_height = new_height
else:
    final_width = int(aspect_ratio * large_size[1])
    final_height = large_size[1]

#resizing the image
imaged = im.resize((final_width, final_height), Image.ANTIALIAS) 

imaged.show()       #to view rthe image
imaged.save("yourModifiedImage", quality=100) #saves the image
