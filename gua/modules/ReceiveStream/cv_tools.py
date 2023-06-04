import cv2

def gen_frames():
    while True:
        success, frame = camera.read()
        if not success: break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'ContentType: image/jpeg\r\n\r\n' + frame + b'\r\n')
