import os
from PIL import Image

image_folder = (r"C:\Users\15023\Documents\CNN\Cienna_training_dresses")

num = 0
for (root, dirs, files) in os.walk(image_folder, topdown=True):

    for name in files:
        print("converting file " + name)
        
        image = Image.open(f'{root}/{name}')
        new_name = str(num)
        
        input_root = "C:\Users\15023\Documents\CNN\Cienna_training_dresses\input"
        output_root = "C:\Users\15023\Documents\CNN\Cienna_training_dresses\output"
        
        image.save(f'{root}/{new_name}.png')
            
        print("saved in " + root + "/" + new_name + ".png")
        num = num + 1
        print("-----------------------")

print("all JPG converted to PNG") 