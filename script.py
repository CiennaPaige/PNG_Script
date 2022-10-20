import os
from PIL import Image

image_folder = (r"C:\Users\15023\Documents\CNN\Cienna_training_dresses")

for (root, dirs, files) in os.walk(image_folder, topdown=True):

    for name in files:
        print("converting file " + name)
        
        image = Image.open(f'{root}/{name}')
        new_name = "output"
        
        image.save(f'{root}/{new_name}.png')
            
        print("saved in " + root + "/" + new_name + ".png")
        print("-----------------------")

print("all JPG converted to PNG") 