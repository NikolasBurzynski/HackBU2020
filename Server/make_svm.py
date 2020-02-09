import os


def makeSVM:
    os.system('cmd /k "python train_model.py --embeddings output/embeddings.pickle --recognizer "'+
               '"output/recognizer.pickle --le output/le.pickle"')
    
def recog(path):
    os.system('cmd /k "python recognize.py --detector face_detection_model --embedding-model "' +
              '"openface_nn4.small2.v1.t7 --recognizer output/recognizer.pickle --le output/le.pickle --image Imgs/Analyze "' + path + '".jpg"')
