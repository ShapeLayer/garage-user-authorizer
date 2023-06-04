from os import listdir
from os.path import join
from keras_facenet import FaceNet
from sklearn import preprocessing, svm
from sklearn.metrics import accuracy_score
from pickle5 import dump as pdump
from joblib import dump as jdump
from sklearn import svm
if __name__ != '__main__':
    from .commons import Face, load_faces, get_embedding
else:
    from commons import Face, load_faces, get_embedding

def load_dataset_each_partition(path: str) -> list[Face]:
    # 'root/train', 'root/val'
    faces_merged: list[Face] = list()
    for subdir in listdir(path): # 'root/train/each', 'root/val/each'
        file: str = join(path, subdir)
        faces: dict = load_faces(file) # 'root/train/each/file', 'root/val/each/file'

        # training phase: ignoreing multiple face detection
        for each in faces:
            now: list = faces[each]
            if len(now) == 0: continue
            face: Face = now[0]
            face.label = subdir
            faces_merged.extend([face])
    return faces_merged

from numpy import ndarray

def load_dataset(model, path: str, postfix: tuple=('train', 'val')) -> tuple[ndarray]:
    # 'root'

    # load dataset partition
    train: list[Face] = load_dataset_each_partition('{path}/{subdir}'.format(
            path = path, subdir = postfix[0]
    ))
    test: list[Face] = load_dataset_each_partition('{path}/{subdir}'.format(
            path = path, subdir = postfix[1]
    ))

    # get embedding
    train_x, train_y, test_x, test_y = list(), list(), list(), list()
    for face in train:
        embedding: ndarray = get_embedding(model, face)
        face.embedding = embedding
        train_x.append(embedding)
        train_y.append(face.label)
    for face in test:
        embedding: ndarray = get_embedding(model, face)
        face.embedding = embedding
        test_x.append(embedding)
        test_y.append(face.label)

    return train_x, train_y, test_x, test_y

def build_model(dataset_path: str, labeler_path: str, classifier_path: str):
    model = FaceNet()
    train_x, train_y, test_x, test_y = load_dataset(model.model, dataset_path)

    in_encoder = preprocessing.Normalizer(norm='l2')
    train_x_transformed = in_encoder.transform(train_x)
    test_x_transformed = in_encoder.transform(test_x)

    out_encoder = preprocessing.LabelEncoder()
    out_encoder.fit(train_y)
    train_y_transformed = out_encoder.transform(train_y)
    test_y_transformed = out_encoder.transform(test_y)

    # output labeler
    file_labeler = open(labeler_path, 'wb')
    pdump(out_encoder, file_labeler)
    file_labeler.close()

    # fitting model
    classifier = svm.SVC(kernel='linear', probability=True)
    classifier.fit(train_x_transformed, train_y_transformed)

    # predict
    yhat_train = classifier.predict(train_x_transformed)
    score_train = accuracy_score(train_y_transformed, yhat_train)
    yhat_test = classifier.predict(test_x_transformed)
    score_test = accuracy_score(test_y_transformed, yhat_test)

    # output classifier
    jdump(classifier, classifier_path)

    print(f'Accuracy: train={score_train * 100}, test={score_test * 100}')

if __name__ == '__main__':
    build_model('../../includes/datasets/demo', '../../includes/trained/demo_labeler.pk1', '../../includes/trained/demo_classifier.pk1')
# build_model(DATASET, f'assets/{DATASET}_labeler.pk1', f'assets/{DATASET}_classifier.pk1')
