from os import path as ospath
from uuid import uuid4 as uuid
from werkzeug.utils import secure_filename

def allowed_filename(filename: str, config: dict) -> bool:
    ALLOWED_EXTENSIONS = config['UPLOAD__PIC_ALLOWED_EXTENSIONS']
    return '.' in filename and \
            get_extension(filename) in ALLOWED_EXTENSIONS

def get_extension(filename: str) -> str:
    return filename.rsplit('.', 1)[1].lower()

def receive_and_save(request, config) -> dict:
    UPLOAD_FOLDER = config['DIR__DATA_USERSTATIC']

    if request.method == 'POST':
        if 'file' not in request.files:
            return {
                'state': 'err',
                'content': 'no file part'
            }
        file = request.files['file']
        if file.filename == '':
            return {
                'state': 'err',
                'content': 'no selected file'
            }
        if file:
            if allowed_filename(file.filename, config):
                filename = secure_filename(file.filename)
                new_filename_uuid = str(uuid())
                new_filename = f'{new_filename_uuid}.{get_extension(filename)}'
                file.save(ospath.join(UPLOAD_FOLDER, new_filename))
                return {
                    'state': 'saved',
                    'file': {
                        'origin': filename,
                        'uploaded': new_filename,
                        'uuid': new_filename_uuid,
                        'request_path': f'/data/userstatic/{new_filename}',
                    },
                    'filename': new_filename
                }
            else:
                return {
                    'state': 'err',
                    'content': 'not allowed file type'
                }
        else:
            return {
                'state': 'err',
                'content': 'operation not done'
            }
