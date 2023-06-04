from os import listdir
from os.path import join
from PIL import Image
from mtcnn.mtcnn import MTCNN
from numpy import asarray, ndarray
from numpy.lib.shape_base import expand_dims

class Face:
    def __init__(self, x: int, y: int, w: int, h: int, face: ndarray, embedding: ndarray=None, label: str=None):
        self.x: int = x
        self.y: int = y
        self.w: int = w
        self.h: int = h
        self.face: ndarray = face
        self.embedding: ndarray = embedding
        self.label: str = label

def extract_face(rgb_vector: ndarray, size: tuple=(160, 160)) -> list[Face]:
    pixels = asarray(rgb_vector)
    model = MTCNN()
    model_query_result = model.detect_faces(pixels)

    faces: list[Face] = []
    for result in model_query_result:
        # process each result box
        x1, y1, w, h = result['box']
        x1, y1 = abs(x1), abs(y1)
        face = pixels[y1:y1+h, x1:x1+w]
        # reform size
        resized = asarray(
                Image.fromarray(face).resize(size)
        )
        faces.append(Face(x1, y1, w, h, resized))
    return faces

def load_faces(path: str) -> dict:
    '''
    :returns: { (filename: str): (face vectors: list[Face]) }
    '''
    facelist = dict()
    for file in listdir(path):
        now = join(path, file)
        image_ndarray: ndarray = asarray(
            Image.open(now).convert('RGB')
        )
        faces: list[Face] = extract_face(image_ndarray)
        facelist[file] = faces
    return facelist

def get_embedding(model, face: Face):
    face_pixels_f32: ndarray = face.face.astype('float32')
    mean, std = face_pixels_f32.mean(), face_pixels_f32.std()

    face_pixels_norm: ndarray = (face_pixels_f32 - mean) / std
    samples = expand_dims(face_pixels_norm, axis=0)
    
    # predict[0] => follow by sklearn spec
    yhat = model.predict(samples)[0]
    return yhat
