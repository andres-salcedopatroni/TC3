import pickle
from deep_translator import GoogleTranslator
import time

#Traducir texto
def traducir(texto):
    traducidos=[]
    for text in texto:
        traducidos.append(GoogleTranslator(source='spanish', target='russian').translate(text))
    return traducidos

#Transformar la data para la red neuronal
def procesar_data(vectorizer,data):
    lista=vectorizer.transform(data)
    lista=lista.toarray()
    return lista

#Obtener una estructura
def obtener(nombre):
    with open(nombre+'.pkl', 'rb') as file:
        return pickle.load(file)
