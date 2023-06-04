'''
Manages `includes/static/alias.json`
'''
from os.path import exists
from json import loads

class StaticAssetsManager:
    def __init__(self, alias_list_path: str):
        self.alias_list_dir = '/'.join(alias_list_path.split('/')[:-1])
        self.index = loads(open(alias_list_path, encoding='utf-8').read())
    
    def get(self, name):
        if name in self.index:
            target = f'{self.alias_list_dir}/{self.index[name]}'
            if exists(target):
                return target
        target = f'{self.alias_list_dir}/{name}'
        if exists(target):
            return target
        raise ValueError('path not found.')
