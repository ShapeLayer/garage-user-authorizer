from os import chdir, mkdir
from os.path import isdir
from subprocess import run
from shutil import copyfile
from json import loads
from .modules.Sqlite3.utils import init as sqlite_init
from .config import config

def init_db():
    return sqlite_init()

def init_front():
    print('[Gua] Start building frontend...')
    chdir('gua/views/front')
    run(['yarn', 'build'])
    chdir('../../../')
    print('[Gua] Frontend built successfully.')
    return

def init_datafile():
    for key in config:
        if not key.startswith('DIR__'): continue
        if not isdir(config[key]):
            mkdir(config[key])

def apply_demo_preset():
    demo_preset_path = config['PRESET__DEMO']
    demo_preset_index = loads(open(f'{demo_preset_path}/index.json').read())
    files = demo_preset_index['files']
    for file in files:
        source_path = '{}/{}'.format(demo_preset_path, file['source'])
        destination_path = '{}/{}'.format(file['dir'], file['filename'])
        copyfile(source_path, destination_path)
