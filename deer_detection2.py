from imageai.Detection import ObjectDetection
import os
import glob
from picamera import PiCamera
from time import sleep

execution_path = os.getcwd()

print("execution_path=",execution_path)

camera = PiCamera()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
detector.loadModel()

print("detector set up")

def scare_deer():
    os.system("mpg321 MountainLionSound.mp3")

def capture_image(file):
    camera.start_preview
    sleep(2)
    camera.capture(file)
    camera.stop_preview
    
def image_detection(detector, input_image, out_image):
    detections = detector.detectObjectsFromImage(input_image=input_image, output_image_path=out_image)
    is_deer = False
    deer = {'sheep','cow','giraffe','horse'}

    for eachObject in detections:
        print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
        name = eachObject["name"]
        is_deer = is_deer or name in deer

    print('is_deer=',is_deer)
    return is_deer

def image_analyzer():
    
    images = glob.glob(execution_path+"/pictures/not_deer/*.jp*g")

    print("images=", images)

    for image in images:
        newimage = image.replace('/not_deer/','/not_deer-new/')
        print(image, newimage)    

        image_detection(detector, image, newimage)  
        print("did image detection: image=", image)

def run(image,newimage):
    while True:
        capture_image(image)
        is_deer = image_detection(detector,image,newimage)
        if is_deer:
            scare_deer()
            print('SHOOT THE DEER!') 

directory = "/home/pi/photos/"
run(directory+"image.jpg", directory+"processed_image.jpg")
