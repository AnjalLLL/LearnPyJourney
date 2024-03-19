from PIL import Image
images = ['Doremon1.gif','Doremon2.gif','Doremon3.gif']
images_as_whole = []
for img in images:
   image = Image.open(img)
   images_as_whole.append(image)


images_as_whole[0].save('Doremon.gif', save_all=True,append_images_as_whole=[images[1:]],duration=200,loop=0)