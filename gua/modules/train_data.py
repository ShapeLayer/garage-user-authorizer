from FaceNet.train import build_model
from FaceNet.IncludesManager.datasets import DatasetsIncludingManager

def train():
    offset = 'gua' if __name__ != '__main__' else '..'
    datasets_path = f'{offset}/includes/datasets'
    outputs_path = f'{offset}/includes/trained'
    datasets_including_manager: DatasetsIncludingManager = DatasetsIncludingManager(f'{datasets_path}/index.json')
    name: str = datasets_including_manager.unzip
    build_model(
        f'{datasets_path}/{name}',
        f'{outputs_path}/{name}_gen_labeler.pk1',
        f'{outputs_path}/{name}_gen_classifier.pk1'
    )

if __name__ == '__main__':
    train()
