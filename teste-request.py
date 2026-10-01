import requests
import json


print("Hello World")

#https://api.trello.com/1/members/me/boards?
#key=fc2b82843957dc8531ea47dede26f020
#&token=ATTA84dbd7e39e04b71389db28588f426dd2d226a092be76f96d75120e733cd84262B9DF3D1B
#&fields-name,shortLink

URL = 'https://api.trello.com/1/members/me/boards'
KEY = 'key=fc2b82843957dc8531ea47dede26f020'
TOKEN = 'token=ATTA84dbd7e39e04b71389db28588f426dd2d226a092be76f96d75120e733cd84262B9DF3D1B'
FIELDS = 'fields=name,shortLink'
url_completa = f'{URL}?{KEY}&{TOKEN}&{FIELDS}'
print(url_completa)

#equivalente a SEND no POSTMAN
resposta = requests.get(url_completa)
print("codigo resposta: ", resposta.status_code)

#Transforma a resposta em JSON
respota_json = json.loads(resposta.text)

#Formtar  JSON para retornar ao print da tela 
retorno = json.dumps(respota_json, indent=2, ensure_ascii=False)
print(retorno)

# PERCORRER LISTA E LISTAR DADOS
lista = json.loads(resposta)
print()
print("A lista contem ", len(lista), "itens")
for item in lista:
    print(item['name'])
