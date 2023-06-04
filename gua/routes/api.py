from flask import Blueprint, request

bp = Blueprint('api_api', __name__, url_prefix='/api/api')

@bp.route('/query/image', methods=['GET'])
def query_image():
    return

@bp.route('/query/videostream', methods=['GET'])
def query_videostream():
    # WIP
    return
