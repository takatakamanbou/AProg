import cv2
from urllib import request

fnCascade = 'haarcascade_frontalface_alt2.xml'
tlabURL = 'https://www-tlab.math.ryukoku.ac.jp/~takataka/course/AProg/'


### 顔検出器の学習済みパラメータを入手する
#
def readCascadeFile():

    print('# ファイル {0} を {1} からダウンロード中...'.format(fnCascade, tlabURL), end='')
    request.urlretrieve(tlabURL+fnCascade, fnCascade)
    print('終了')
    print('# このファイルのライセンスについては，ファイルの先頭に記されています')


### 機械学習による顔検出の仕組み
#
def facedetect(image):

    # 顔検出器の初期化
    classifier = cv2.CascadeClassifier(fnCascade)

    # グレイスケール画像を用意する
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # グレイスケール画像から顔を検出
    result = classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(32, 32))

    # [ [ 1人目の顔の左上の位置（X座標）, 左上の位置（Y座標）, 幅, 高さ ],
    #   [ 2人目の顔の左上の位置（X座標）, 左上の位置（Y座標）, 幅, 高さ ],..., ]
    # というリストを作って return する．1人しか検出しなくても，戻り値は
    # [ [ 100, 50, 30, 30] ]  のようにリストのリストになることに注意
    rv = []
    for v in result:
        rv.append(list(v))

    return rv


if __name__ == '__main__':

    import os

    if os.path.isfile(fnCascade):
        print(f'# ファイル {fnCascade} はダウンロード済みのようです')
    else:
        readCascadeFile()
