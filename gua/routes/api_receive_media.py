from flask import Blueprint, Response, request, flash, current_app
from werkzeug.utils import secure_filename
from uuid import uuid4 as uuid
from json import dumps
from ..modules.File.receive import receive_and_save
from ..modules.FaceNet.predict import predict

bp = Blueprint('api__receive_media', __name__, url_prefix='/api/receive_media')

def allowed_filename(filename: str) -> bool:
    config = current_app.config
    ALLOWED_EXTENSIONS = config['UPLOAD__PIC_ALLOWED_EXTENSIONS']
    return '.' in filename and \
            get_extension(filename) in ALLOWED_EXTENSIONS

def get_extension(filename: str) -> str:
    return filename.rsplit('.', 1)[1].lower()

@bp.route('/video_feed')
def video_feed():
    '''return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')'''
    return

@bp.route('/image_file', methods=['GET', 'POST'])
def image_file():
    config = current_app.config

    print('savestart')
    # Receive imagefile and save to temporary files directory
    operations = receive_and_save(request, config)
    print('savereturned')
    if operations['state'] == 'err':
        flash('err: {}'.format(operations['content']))
    print('saved')
    if operations['state'] != 'saved':
        return dumps(operations)
    print('aftersave')

    
    print('predict_start')
    print('target: ' + operations['file']['request_path'][1:])
    predict_result = predict(operations['file']['request_path'][1:])
    operations['state'] = 'predict_done'
    operations['predict'] = predict_result
    print('predict_done')

    return dumps(operations)
