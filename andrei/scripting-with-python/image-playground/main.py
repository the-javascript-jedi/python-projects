# use PILLOW Library
from PIL import Image,ImageFilter

img=Image.open('./Pokedex/pikachu.jpg')

print("img",img)
print("img.format",img.format)
print("img.size",img.size)
print("img.mode",img.mode) #RGB

# apply filters to an image
filtered_img=img.filter(ImageFilter.BLUR)
# save the filtered image - png will only support this filter
filtered_img.save("blur.png","png")

# convert the type of an image
converted_img=img.convert('L')
converted_img.save("grey.png","png")


# rotate the image
crooked=filtered_img.rotate(180)
crooked.save("crooked.png","png")

# resize the image
resize=filtered_img.resize((300,300))
resize.save("resize.png","png")

# crop the image
box=(100,100,400,400)
cropped=filtered_img.crop(box)
cropped.save("cropped.png","png")

# display the image
# filtered_img.show()

# creating a thumbnail
imageToConvert=Image.open("./Pokedex/bulbasaur.jpg")
img.thumbnail((200,200))
img.save('thumbnail.jpg')