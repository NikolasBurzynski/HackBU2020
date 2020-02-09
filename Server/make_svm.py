import os


def makeSVM:
    os.system('cmd /k "python train_model.py --embeddings output/embeddings.pickle --recognizer "'+
               '"output/recognizer.pickle --le output/le.pickle"')
    
