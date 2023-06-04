# Garage user authorizer

[![Codefactor grade](https://www.codefactor.io/repository/github/shapelayer/garage-user-authorizer/badge)](https://www.codefactor.io/repository/github/shapelayer/garage-user-authorizer) [![DeepScan grade](https://deepscan.io/api/teams/20682/projects/24076/branches/738930/badge/grade.svg)](https://deepscan.io/dashboard#view=project&tid=20682&pid=24076&bid=738930)  
_Vision AI libraries training: with MTCNN, FaceNet_  

![demo](/.github/static/demo.png)  

Garage user authorizer (Gua)는 비전 AI 라이브러리의 구체적인 활용 안을 구현하는 것을 목표로 작성된 데모입니다.  
이 데모는 허가된 고정 출입자만 통과시키는 출입 통제 시스템에 얼굴 인식 및 인물 검색 기능을 도입했습니다.  

## 주의, 개발이 일정 수준 이상 완료되지 않았습니다.
[![](https://img.shields.io/badge/status-work%20in%20progress-red)](#)  

이 데모는 작업 중으로, 실행하더라도 일부 기능이 실행되지 않거나 오작동할 수 있습니다.  

## 별첨
[Jupyter Notebook](/notebook/)  
 * [MTCNN, FaceNet 전체 작동 과정 테스트 결과 - `/notebook/FaceNet.ipynb`](/notebook/FaceNet.ipynb)

## 리포지토리 주요 디렉토리
 * [프론트엔드: `gua/views/front/`](/gua/views/front/)
 * [백엔드: `gua/`](/gua/)

## 시작하기
### 1. 런타임 구성
이 애플리케이션은 Python과 Node.js 런타임을 사용합니다. 각 언어의 런타임 설치 가이드를 참조하여 런타임 구성을 완료하세요.

 * [Python](https://www.python.org/downloads/)
 * [Node.js](https://nodejs.org/ko/download/)

### 2. 의존성 설치

이 애플리케이션은 각종 의존성 모듈을 참조하고 있습니다.  
다음 명령을 통해 의존성 모듈을 모두 설치하세요.  

```sh
python tools/init.py
```

### 3. 서버 실행

아래 명령을 통해 서버를 실행할 수 있습니다.  

```sh
python -m flask --app gua run
```

## 외부 저작물 사용
 * [SUIT](https://sunn.us/suit/) - 폰트 - _SIL Open Font License_
 * [5 Celebrity Faces Dataset](https://www.kaggle.com/datasets/dansbecker/5-celebrity-faces-dataset) - 이미지 데이터셋 - _학습에 사용_

## Troubleshooting
* `ImportError: libGL.so.1: cannot open shared object file: No such file or directory` 오류가 발생합니다. : 로컬에 `libgl1-mesa-glx` 패키지를 설치합니다.
* 그 외 문제 상황이 있나요? [이슈트래커](https://github.com/ShapeLayer/garage-user-authorizer)에 문제 상황을 자세히 알려주세요!
