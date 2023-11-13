from flask import Flask
from funciones_app import *
from flask import request
from funciones_app import *

app = Flask(__name__)


@app.route('/api', methods=['GET', 'POST'])
def clasificar():
    if request.method == 'POST':
        datos=request.get_json()
        #tweets=obtener_tweets(datos['usuarios'])
        vec=obtener('vectorizer')
        red=obtener('red')
        respuesta=[]
        for t in datos:
            if(len(t[2])>0):
                texto=traducir(t[2])
                print(t[0],texto)
                data=procesar_data(vec,texto)
                print(data)
                resul=red.predict(data).tolist()
                print(resul)
                lis=[]
                for i in range(len(resul)):
                    lis.append([t[1][i],t[2][i],resul[i]])
                respuesta.append([t[0],lis])
        json={'respuesta':respuesta}
        return json
    else:
        return []

if __name__=="__main__":
    app.run()
    