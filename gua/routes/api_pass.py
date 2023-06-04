from flask import Blueprint, request
from ..modules.Sqlite3.utils import get_con
from json import dumps
from datetime import datetime, date
from time import mktime
from uuid import uuid4 as uuid

bp = Blueprint('api_pass', __name__, url_prefix='/api/pass')

@bp.route('/reserved/get', methods=['GET'])
def pass_reserved_get():
    starts: float = request.args.get('starts', datetime.now().timestamp())
    ends: float = request.args.get('ends', mktime(date(2999, 12, 31).timetuple()))
    limit: int = request.args.get('limit', 10)

    con, cur = get_con()
    cur.execute('''
        SELECT * FROM pass_reserved
        WHERE timeat >= ? AND timeat <= ?
        LIMIT ?;
    ''', [starts, ends, limit])
    res = cur.fetchall()
    con.close()

    return dumps({
        'state': 'success',
        'body': [
            {
                'event_id': row[0],
                'passer': row[1],
                'related': row[2],
                'timeat': row[3],
                'description': row[4]
            }
        for row in res]
    })

@bp.route('/reserved/put', methods=['GET', 'POST'])
def pass_reserved_put():
    if request.method == 'GET':
        return dumps({
            'state': 'error',
            'error': 'form params required.'
        })
    elif request.method == 'POST':
        form = request.form.to_dict
        for key in ['passer', 'related', 'timeat', 'description']:
            if key not in form:
                return dumps({
                    'state': 'error',
                    'error': f'{key} not received.'
                })
        event_id = str(uuid())
            
        con, cur = get_con()
        cur.execute('''
            INSERT INTO pass_reserved (event_id, passer, related, timeat, description)
            VALUES(?, ?, ?, ?, ?);
        ''', [event_id, form['passer'], form['related'], form['timeat'], form['description']])
        con.commit()
        con.close()
        return dumps({
            'state': 'success',
            'event_id': event_id
        })
