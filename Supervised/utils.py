# model persistance
import pickle

def save_model(modelObj, pathToSave):
    with open(pathToSave,'wb') as f:
        pickle.dump(modelObj,f)
        print('model saved')

def load_model(path_to_model):
    with open(path_to_model,'rb') as f:
        return pickle.load(f)