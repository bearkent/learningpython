from imageai.Detection import ObjectDetection
import RPi.GPIO as gpio
import os
import os.path
import glob
from picamera import PiCamera
from time import sleep
import sys

execution_path = os.getcwd()

print("execution_path=", execution_path)

camera = PiCamera()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
detector.loadModel()

os.system("amixer cset numid=3 1")

spray_time = 30

light_pin = 26
sprinkler_pin = 20

gpio.setmode(gpio.BCM)
gpio.setup(light_pin, gpio.OUT)
gpio.setup(sprinkler_pin, gpio.OUT)


print("detector set up")

def scare_deer():
    os.system("mpg321 MountainLionSound.mp3")

spray_time = 30

light_pin = 20
sprinkler_pin = 26

not_deer_pictures   =  "/pictures/not_deer/*.jp*g"
analyzed_not_deer_pictures  = '/not_deer/', '/not_deer-new/'

gpio.setmode(gpio.BCM)
gpio.setup(light_pin, gpio.OUT)
gpio.setup(sprinkler_pin, gpio.OUT)

def shoot_deer():
    gpio.output(sprinkler_pin, gpio.HIGH)
    gpio.output(light_pin, gpio.HIGH)
    sleep(spray_time)
    gpio.output(sprinkler_pin, gpio.LOW)
    gpio.output(light_pin, gpio.LOW)

def capture_images(dir):
    for i in range(0,11):
        file = dir+"/image_"+str(i)+".jpg"
        capture_image(file)
        sleep(2)

def capture_image(file):
    camera.start_preview
    sleep(2)
    print('Taking a picture')
    camera.capture(file)
    camera.stop_preview
        
def image_detection(detector, input_image, out_image):
    print('analyzing photo')
    detections = detector.detectObjectsFromImage(input_image=input_image, output_image_path=out_image)
    is_deer = False
    #the image detection code said a deer were these animals the most often
    deer = {'sheep','cow','giraffe','horse'}

    for eachObject in detections:
        print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
        name = eachObject["name"]
        is_deer = is_deer or name in deer

   #prints if the picture is a deer

    print('is_deer=', is_deer, ' file=', out_image)
    return is_deer
    print(name)
#unused function

def image_analyzer(indir, outdir):
    
    images = glob.glob(indir + "/*.jp*g")

    print("images=", images)

    for image in images:
        newimage = outdir + '/' + os.path.basename(image)
        print(image, newimage)    

        image_detection(detector, image, newimage)  
        print("did image detection: image=", image)

def run(image, newimage):
    while True:
        capture_image(image)
        is_deer = image_detection(detector, image,newimage)
        if is_deer:
            scare_deer()
            sleep(20)
            shoot_deer() 


mode = sys.argv[1]

directory = '/home/pi/photos/'

try:
    if mode == "run":
        print("running")
        run(directory+"image.jpg", directory+"processed_image.jpg")
    elif mode == "images":
        dir = sys.argv[2]
        print("Taking pictures Dir="+dir)
        capture_images(dir)
    elif mode == "analyze":
        indir = sys.argv[2]
        outdir = sys.argv[3]
        print("Analyzing pictures Indir="+indir + " Outdir=" + outdir)
        image_analyzer(indir, outdir)
    else:
        raise NameError("Unkown mode.  mode=" + mode)

finally:
        gpio.cleanup()
