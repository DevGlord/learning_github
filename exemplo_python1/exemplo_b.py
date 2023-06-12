import json

LOCAL_ARQUIVO = 'ex1.json'

with open(LOCAL_ARQUIVO,'r') as arquivo:
    print(json.load(arquivo))