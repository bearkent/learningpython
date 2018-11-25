from imageai.Detection import ObjectDetection
import os
import glob

execution_path = os.getcwd()

print("execution_path=",execution_path)

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
detector.loadModel()

print("detector set up")

def image_detection(detector, input_image, out_image):
    detections = detector.detectObjectsFromImage(input_image=input_image, output_image_path=out_image)

    for eachObject in detections:
        print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
    
    
images = glob.glob(execution_path+"/pictures/deer/*.jp*g")

print("images=", images)

for image in images:
    newimage = image.replace('/deer/','/deer-new/')
    print(image, newimage)    

    image_detection(detector, image, newimage)  
    print("did image detection: image=", image)
    
