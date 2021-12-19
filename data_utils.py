import requests
from io import BytesIO
from PIL import Image

class DataUtils:
    def __init__(self):
        pass

    def get_training_data(self):
        f = open("C:/Users/cata0/OneDrive/Desktop/School/3rdYear/Computer Vision & Deep Learning/Project/training_dataset/images.txt", "r")
        x = []
        y = []
        #maximum = 0 => 6181    |
        #minimum = 10000 => 0   | => 6182 classes
        for line in f:
            image_id, class_id = line.split(" ")
            class_id = int(class_id)
            #maximum = max(maximum, class_id)
            #minimum = min(minimum, class_id)
            x.append(image_id)
            y.append(class_id)
            #print(image_id)
            
        #print(minimum)
        #print(maximum)
        #print(len(x))  | => 247260 images 
        return x, y

    def get_classes(self):
        f = open("C:/Users/cata0/OneDrive/Desktop/School/3rdYear/Computer Vision & Deep Learning/Project/training_dataset/classes.txt", "r")
        classes = []
        for imageClass in f:
            classes.append(imageClass)

        return classes

    def get_image_with_id(self, image_id):
        image_url = "https://bs.plantnet.org/image/o/" + image_id
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))
        return image.convert('RGB')

    
#x, y = get_training_data()
#data_utils = DataUtils()
#image0 = data_utils.get_image_with_id("37837eeee3a52c9720f03f8e7ef562d8939566d2")
#image0.show()

