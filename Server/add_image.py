import os

def add_img(path):
    os.system('cmd /k "python extract_embeddings.py --image "' + path +
              '" --embeddings output/embeddings.pickle --detector face_detection_model --embedding-model openface_nn4.small2.v1.t7"')
