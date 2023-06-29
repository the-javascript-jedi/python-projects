# to run program - python JpgToPngConverter.py Pokedex/ new/
import sys
import os
from PIL import Image

# grab first and second argument
image_folder=sys.argv[1]
output_folder=sys.argv[2]

print(image_folder,output_folder)
# check if new folder exists, if not create the folder
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through entire folder and convert the images to png
for filename in os.listdir(image_folder):
    img=Image.open(f'{image_folder}{filename}')
    # remove existing .jpg in filename and append png
    clean_name=os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png','png')
    print('all done')