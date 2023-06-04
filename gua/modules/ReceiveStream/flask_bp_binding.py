from flask import Blueprint, Response, request, flash, current_app
from werkzeug.utils import secure_filename
from .cv_tools import gen_frames
from uuid import uuid4 as uuid
from ..File.receive import receive_and_save
from json import dumps

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
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
