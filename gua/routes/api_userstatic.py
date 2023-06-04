from flask import Blueprint, send_file, current_app

bp = Blueprint('api_userstatic', __name__, url_prefix='/api/userstatic')

@bp.route('/<path:path>', methods=['GET'])
def index(path = ''):
    config = current_app.config
    return send_file('{offset}/{dir}/{filename}'.format(
        offset='..',
        dir=config['DIR__DATA_USERSTATIC'],
        filename=path
    ))

