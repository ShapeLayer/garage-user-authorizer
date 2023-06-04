from os.path import exists
import sqlite3
from json import loads

config = loads(open('gua/config.json', encoding='utf-8').read())
dir = config['DIR__DATA_DB']
file = config['FILE__SQLITE']
path = f'{dir}/{file}'
SCRIPT_PATH = 'gua/modules/Sqlite3/scripts'

def get_con():
    con = sqlite3.connect(path, check_same_thread = False)
    cur = con.cursor()
    return con, cur

def init():
    if exists(path): return
    con, cur = get_con()
    with open(f'{SCRIPT_PATH}/init.sql', encoding='utf-8') as f:
        cur.executescript(f.read())
    with open(f'{SCRIPT_PATH}/demo.sql', encoding='utf-8') as f:
        cur.executescript(f.read())
    con.commit()
    con.close()
