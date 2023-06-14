import json
from exemplo12 import LOCAL_ARQUIVO,Paises



with open(LOCAL_ARQUIVO,'r',encoding='utf8') as arquivo:
    print(json.load(arquivo))
