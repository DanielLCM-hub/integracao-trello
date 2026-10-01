import requests
import json

#DEFINIR VARIVEIS JSON
objeto_json = {}
#LISTA SEMPRE SERÁ "[]"
lista_json = [] 

objeto_json= {
    "coluna1": "valor1",
    "coluna2": "valor2"
}
print("Valor do campo coluna1: ", objeto_json['coluna1'])

lista_json = [
    {
        "coluna1": "valor1",
        "coluna2": "valor2",
        'detalhes': {
            'valor': 1
        },
    },
    {
        "coluna1": "valor3",
        "coluna2": "valor4",
        'detalhes': {
            'valor': 2
        },
    },
]
print("Valor do campo 2 da lista: ", lista_json[1]['coluna2'])
print(lista_json[2]['detalhes']['valor'])
print(lista_json[0:2])