from flask import Flask, Blueprint, send_from_directory

bp = Blueprint('front_bridge', __name__)

svelte_app_path = 'views/front/build'

@bp.route('/')
@bp.route('/<path:path>')
def index(path = ''):
    if path == '' or path[-1] == '/': 
        return send_from_directory(f'{svelte_app_path}', 'index.html')
    else:
        url_parsed = path.split('/')
        req_loc = '{svelte_app_path}/{file_location}'.format(svelte_app_path=svelte_app_path, file_location='/'.join(url_parsed[:-1]))
        req_file = url_parsed[-1]
        if '.' not in req_file: req_file += '.html'
        return send_from_directory(req_loc, req_file)
