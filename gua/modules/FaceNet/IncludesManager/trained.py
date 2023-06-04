'''
Manages `includes/trained/index.json`
'''
from json import loads
from joblib import load as jload

class TrainedIncludingManager:
    def __init__(self, dataset_index_path: str):
        self.dataset_index_dir = '/'.join(dataset_index_path.split('/')[:-1])
        index = loads(open(dataset_index_path, encoding='utf8').read())
        self.current: str = index['current']
        self.classifier_config: dict = index[self.current]['classifier']
        self.classifier_path: str = self.classifier_config['path']
        self._classifier = None
        self.labeler_config: dict = index[self.current]['labeler']
        self.labeler_path: str = self.classifier_config['path']
        self._labeler = None
    
    @property
    def classifier(self):
        if self._classifier == None:
            self._classifier = self.load_pk1(
                self.relpath_to_abspath(self.classifier_path)
            )
        return self._classifier
    
    @property
    def labeler(self):
        if self._labeler == None:
            self._labeler = self.load_pk1(
                self.relpath_to_abspath(self.labeler_path)
            )
        return self._labeler

    def relpath_to_abspath(self, path: str):
        # based on `includes` dir path
        return f'{self.dataset_index_dir}/{path}'

    def load_pk1(self, path: str):
        return jload(path)
