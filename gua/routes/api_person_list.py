from flask import Blueprint, request
from ..modules.Sqlite3.utils import get_con
from json import dumps

bp = Blueprint('api_person_list', __name__, url_prefix='/api/person_list')

@bp.route('/get', methods=['GET'])
def user_get():
    req_id = request.args.get('id')
    if req_id == None:
        return dumps({
            'state': 'error',
            'error': 'id field is none'
        })
    con, cur = get_con()
    cur.execute('''
        SELECT id, probability, description FROM person_list_facenet_each_person
        WHERE event_id = ?
    ''', [req_id])
    res = cur.fetchall()
    if len(res) == 0:
        return dumps({
            'state': 'error',
            'error': 'relates not found'
        })
    relates = []
    for row in res:
        now_person_id = row[0]
        relate = {
            'id': row[0],
            'probability': row[1],
            'description': row[2]
        }

        # ID로 각 인물 객체 로드
        cur.execute('''
            SELECT name, image_path FROM users
            WHERE id = ?
        ''', [now_person_id])
        res_user = cur.fetchall()
        if len(res_user) == 0:
            return dumps({
                'state': 'error',
                'error': 'internal error',
                'code': 'PERSON_NOT_FOUND',
                'detail': '각 사건(사람 리스트)와 실제 사람 객체를 매치하는 과정에서 기록된 사람 객체 ID에 해당하는 객체가 DB에서 검색되지 않았습니다.'
            })
        user = res_user[0]
        relate['name'] = user[0]
        relate['image_path'] = user[1]

        # ID로 인물의 소속 조직 로드
        cur.execute('''
            SELECT user.id, user.name FROM users AS user
            INNER JOIN organization as org
            ON org.org_user_id = user.id
            WHERE org.user_id = ?;
        ''', [now_person_id])
        res_org = cur.fetchall()
        if len(res_org) == 0:
            relate['organization'] = {
                'id': 'NIL',
                'display_name': ''
            }
        else:
            relate['organization'] = {
                'id': res_org[0],
                'display_name': res_org[1]
            }
        relates.append(relate)
    return dumps({
        'state': 'success',
        'result': {
            'event_id': req_id,
            'related': relates
        }
    })

@bp.route('/index', methods=['GET'])
def person_list():
    req_lim = request.args.get('limits', 10)
    req_id = request.args.get('id', None)
    con, cur = get_con()
    cur.execute('''
        SELECT DISTINCT id, invoked FROM person_list_facenet
        {}
        ORDER BY invoked DESC
        LIMIT ?;
    '''.format('WHERE id = ?' if req_id else ''),
        [req_id, req_lim] if req_id else [req_lim]
    )
    res = cur.fetchall()
    return dumps({
        'state': 'success',
        'result': [{
            'id': row[0],
            'invoked': row[1]
        } for row in res]
    })

