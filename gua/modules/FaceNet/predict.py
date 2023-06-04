from keras_facenet import FaceNet
from sklearn import preprocessing
from numpy import asarray, ndarray, expand_dims
from PIL import Image, ImageDraw, ImageFont
from joblib import load as jload
from matplotlib.pyplot import imshow
if __name__ != '__main__':
    from .commons import extract_face, get_embedding, Face
    from .IncludesManager.trained import TrainedIncludingManager
    from .IncludesManager.static_assets import StaticAssetsManager
else:
    from commons import extract_face, get_embedding, Face
    from IncludesManager.trained import TrainedIncludingManager
    from IncludesManager.static_assets import StaticAssetsManager

# fix later hard-coded path
# * bug: labeler returns trained_including yields error related with svc property undefined.
if __name__ != '__main__':
    trained_including = TrainedIncludingManager('gua/includes/trained/index.json')
    static_including = StaticAssetsManager('gua/includes/static/alias.json')
else:
    trained_including = TrainedIncludingManager('../../includes/trained/index.json')
    static_including = StaticAssetsManager('../../includes/static/alias.json')

if __name__ != '__main__':
    classifier = jload('gua/includes/trained/demo_classifier.pk1') #trained_including.classifier
    labeler = jload('gua/includes/trained/demo_labeler.pk1') #trained_including.labeler
else:
    classifier = jload('../../includes/trained/demo_classifier.pk1') #trained_including.classifier
    labeler = jload('../../includes/trained/demo_labeler.pk1') #trained_including.labeler

def predict(filepath: str):
    from os import getcwd
    image: Image = Image.open(filepath).convert('RGB')
    image_ndarray: ndarray = asarray(image)
    model = FaceNet()
    faces: list[Face] = extract_face(image_ndarray)

    in_encoder = preprocessing.Normalizer(norm='l2')

    # * TODO: return results in for loop..
    # Fix to support multiple face
    for face in faces:
        embedding: ndarray = expand_dims(get_embedding(model.model, face), axis=0)

        # use scikit-learn
        face.embedding = in_encoder.transform(embedding)

        # classify
        yhat: ndarray = classifier.predict(embedding)
        prob: ndarray = classifier.predict_proba(embedding)
        label: ndarray = labeler.inverse_transform(yhat)

        '''
        # draw result
        draw: ImageDraw = ImageDraw.Draw(image)
        draw.rectangle(((face.x, face.y), (face.x + face.w, face.y + face.h)), outline=(255, 0, 0), width=3)
        draw.rectangle(((face.x, face.y), (face.x + face.w // 2, face.y - face.h // 10)), fill=(255, 0, 0))
        font: ImageFont = ImageFont.truetype(static_including.get('suit'))
        draw.text((face.x, face.y - face.h // 10), label[0], fill=(255, 255, 255), font=font)
        imshow(asarray(image.convert('RGB')))
        '''
 
        # print result
        buf = []
        buf.append(f'label: {label[0]}')
        buf.append(f'prob: {prob[0][yhat][0]*100}')
        # print('\n'.join(buf))
        return {
            'label': label[0],
            'prob': prob[0][yhat][0]*100,
            'face': { 'x': face.x, 'y': face.y, 'w': face.w, 'h': face.h }
        }

# predict(f'{PATH}/assets/target.jpg')
if __name__ == '__main__':
    predict('../../../data/userstatic/1fe97842-7ad5-4f02-873e-c3fd47430144.jpeg')
