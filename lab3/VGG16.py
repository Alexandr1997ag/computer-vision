import torch
from datetime import datetime

now = datetime.now()
model = torch.hub.load( 'pytorch/vision:v0.10.0','vgg11', pretrained=True)

# Second, put the network in eval mode
model.eval()

# Third, carry out model inference
from torchvision import transforms
transform = transforms.Compose([            #[1]
 transforms.Resize(224),                    #[2]
 transforms.CenterCrop(224),                #[3]
 transforms.ToTensor(),                     #[4]
 transforms.Normalize(                      #[5]
 mean=[0.485, 0.456, 0.406],                #[6]
 std=[0.229, 0.224, 0.225]                  #[7]
 )])

from PIL import Image
img = Image.open("dog.jpg")

img_t = transform(img)
batch_t = torch.unsqueeze(img_t, 0)

out = model(batch_t)

with open('imagenet_classes.txt') as f:
 classes = [line.strip() for line in f.readlines()]

_, index = torch.max(out, 1)

percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100

print(classes[index[0]], percentage[index[0]].item())

_, indices = torch.sort(out, descending=True)
[(classes[idx], percentage[idx].item()) for idx in indices[0][:5]]
now1 = datetime.now()
t = now1-now
print(t)
#
# from tensorflow.keras.applications.vgg16 import VGG16
# from tensorflow.keras.preprocessing import image
# from tensorflow.keras.applications.vgg16 import preprocess_input
# import numpy as np
#
# model = VGG16(weights='imagenet', include_top=False)
#
# img_path = 'dog.jpg'
# img = image.load_img(img_path, target_size=(224, 224))
# x = image.img_to_array(img)
# x = np.expand_dims(x, axis=0)
# x = preprocess_input(x)
#
# preds = model.predict_classes(np.expand_dims(image, axis=0))[0]
#
# print('Predicted Label',preds)