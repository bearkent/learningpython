from picamera import PiCamera
from time import sleep

camera = PiCamera()

def capture_image(file):
    camera.start_preview
    sleep(2)
    camera.capture(file)
    camera.stop_preview

capture_image('./image.jpg')



