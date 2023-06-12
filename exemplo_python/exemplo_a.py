import json
LOCAL_ARQUIVO = 'aprimorando.json'

with open(LOCAL_ARQUIVO,'r') as arquivo:
    print(json.load(arquivo))