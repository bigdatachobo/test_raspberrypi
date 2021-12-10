from flask import Flask
from flask.wrappers import Response
import cv2 as cv
import threading

# global variabl

app = Flask(__name__) #flask 인스턴스화 시킴
@app.route("/")

def helloworld():
    str = """
    Hello World!<br>I'm working on the Raspberry Pi 4 !!!
    """
    return str

global video_frame
def encodeframe():
    global video_frame
    while True:
        ret, encoded_image = cv.imencode('.jpg', video_frame)
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encoded_image) + b'\r\n')
    return

@app.route('/streaming')
def streamframe():
    return Response(encodeframe(), mimetype='multipart/x-mixed-replace; boundary=frame')
    
# /dev/video0/ 장치 경로
def captureframe():
    global video_frame
    cap = cv.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        video_frame = frame.copy()
        # cv.imshow('webcam', frame)
        cv.waitKey(30)
        pass
    return

if __name__ == '__main__':

    cap_thread = threading.Thread(target=captureframe)
    cap_thread.daemon = True
    cap_thread.start()
    
    app.run(host='0.0.0.0', port='8000') #host = ip
    # cap_thread.join()