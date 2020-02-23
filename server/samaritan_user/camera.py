import threading
import time

from picamera.array import PiRGBArray
from picamera import PiCamera
from picamera import PiCamera
import cv2

# initialize the camera and grab a reference to the raw camera capture

class CustomPiCam(object):

    def __init__(self):
        camera = PiCamera()
        camera.resolution = (480, 480)
        camera.framerate = 32
        camera_width, camera_height = 480, 480
        rawCapture = PiRGBArray(camera, size=(camera_width, camera_height))

        time.sleep(0.1)

        self.camera_stream = camera.capture_continuous(rawCapture, format="bgr", use_video_port=True)
        threading.Thread(target=self.update, args=()).start()

    def get_frame(self):
        image = self.frame
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            self.frame = next(self.camera_stream).array

