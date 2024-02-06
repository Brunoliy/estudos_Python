import json

dicionario = {'brn':['BRUNO', '123', '14/06', 'REC_01']}

with open ("bd1.json", "w") as json_file:
    json.dump(dicionario, json_file)

