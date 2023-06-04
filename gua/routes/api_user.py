from flask import Blueprint, request
from ..modules.Sqlite3.utils import get_con
from json import dumps

bp = Blueprint('api_user', __name__, url_prefix='/api/user')

@bp.route('/get', methods=['GET'])
def user_get():
    req_id = request.args.get('id')
    if req_id == None:
        return dumps({
            'state': 'error',
            'error': 'id field is none'
        })
    con, cur = get_con()
    cur.execute('SELECT * FROM users WHERE id = ?', [req_id])
    res = cur.fetchall()
    if len(res) != 0:
        return dumps({
            'state': 'success',
            'id': res[0][0],
            'name': res[0][1],
            'acl': res[0][2],
            'user_type': res[0][3],
            'image_path': res[0][4]
        })
    return dumps({
        'state': 'error',
        'error': 'not found'
    })
