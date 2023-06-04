# Notebook

 * [FaceNet.ipynb](./FaceNet.ipynb) - 얼굴 분류 학습 결과 노트북
 * [assets](./assets)
   * SUIT-Variable.ttf
   * target.jpg
   * demo_classifier.pk1 - Classifier
   * demo_labeler.pk1 - Labeler

## FaceNet 노트북 결과 해석
 * MTCNN(얼굴 추출 모델)은 얼굴을 제대로 판단하여 이미지 위에 결과를 표시함
 * FaceNet(얼굴 인식 모델)은 추출된 얼굴을 제대로 인식함: 이미지 상의 `dbdfb375-c57a-4086-a0bb-906ffa393973`는 데이터 셋이 작성자의 얼굴에 부여한 UUID임
 * FaceNet의 `prob` 값이 낮은 것은 사진 속 인물이 마스크를 착용하고 있기 때문임
