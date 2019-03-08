import cv2
import os
import numpy as np
from PIL import Image 

recognizer = cv2.createLBPHFaceRecognizer()
cascadePath = "Classifiers/face.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
path = 'DataSet'

def get_images_and_labels(path):
     image_paths = [os.path.join(path, f) for f in os.listdir(path)]
     images = []
     labels = []
     for image_path in image_paths:
         image_pil = Image.open(image_path).convert('L')
         image = np.array(image_pil, 'uint8')
         Id = int(os.path.split(image_path)[1].split(".")[0].replace("ID-", ""))
         print Id
         faces = faceCascade.detectMultiScale(image)
         for (x, y, w, h) in faces:
             images.append(image[y: y + h, x: x + w])
             labels.append(Id)
     print "all generated"
     return images, labels


images, labels = get_images_and_labels(path)
cv2.waitKey(1)

recognizer.train(images, np.array(labels))
recognizer.save('Trainer/trainer.yml')
