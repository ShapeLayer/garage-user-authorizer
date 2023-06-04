'''
Manages `includes/datasets/index.json`
'''
from json import loads

class DatasetsIncludingManager:
    def __init__(self, dataset_index_path: str):
        self.dataset_index_dir = '/'.join(dataset_index_path.split('/')[:-1])
        index = loads(open(dataset_index_path, encoding='utf8').read())
        self.current: str = index['current']
        self.current_dataset: dict = index[self.current]
        self.zip: str = self.current_dataset['zip']
        self.unzip: str = self.current_dataset['unzip']
        self.load_struct_info()

    def load_struct_info(self):
        if self.current_dataset['struct_index_included']:
            curr_index_path: str = self.relpath_to_abspath(f'{self.unzip}/index.json')
            curr_index: dict = loads(open(curr_index_path, encoding='utf-8').read())
            self.struct = curr_index['struct']
        else:
            self.struct = self.current_dataset['struct_index_included']

    def relpath_to_abspath(self, path: str):
        # based on `includes` dir path
        return f'{self.dataset_index_dir}/{path}'
