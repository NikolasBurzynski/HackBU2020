import os

def initialize(path):
    os.system('cmd /k "python extract_embeddings_initial.py --dataset "' + path +
              '" --embeddings output/embeddings.pickle --detector face_detection_model --embedding-model openface_nn4.small2.v1.t7"')

def add_img(path):
    os.system('cmd /k "python extract_embeddings.py --image "' + path +
              '" --embeddings output/embeddings.pickle --detector face_detection_model --embedding-model openface_nn4.small2.v1.t7"')

def train_svm():
    os.system('cmd /k "python train_model.py --embeddings output/embeddings.pickle --recognizer "'+
               '"output/recognizer.pickle --le output/le.pickle"')

def recog(path):
    os.system('cmd /k "python recognize.py --detector face_detection_model --embedding-model "' +
              '"openface_nn4.small2.v1.t7 --recognizer output/recognizer.pickle --le output/le.pickle --image "' + path)
