import requests
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    url = "https://gist.githubusercontent.com/reroes/502d11c95f1f8a17d300ece914464c57/raw/872172ebb60e22e95baf8f50e2472551f49311ff/gistfile1.txt"
    response = requests.get(url)

    numeros = ('3','4','5','7')

    archivo = response.text
    archivo = archivo.splitlines()

    cabezeras = archivo[0].split("|")

    archivo = list(filter(lambda linea: linea.startswith(numeros), archivo))
    # archivo = [ linea for linea in archivo if linea.strip().startswith(numeros) ]

    html = (""
            "<h1>Listado</h1>"
            f"Conteo de personas: {len(archivo)} "
            "<hr>"
            f"<table><tr><th>{cabezeras[0].upper()}</th>"
            f"<th>{cabezeras[1].upper()}</th>"
            f"<th>{cabezeras[2].upper()}</th>"
            f"<th>{cabezeras[3].upper()}</th>"
            f"<th>{cabezeras[4].upper()}</th></tr>")

    for linea in archivo:
        linea_separada = linea.split("|")
        html += (f"<tr><td>{linea_separada[0]}</td>"
                 f"<td>{linea_separada[1]}</td>"
                 f"<td>{linea_separada[2]}</td>"
                 f"<td>{linea_separada[3]}</td>"
                 f"<td>{linea_separada[4]}</td></tr>")

    html += "</table>"

    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)