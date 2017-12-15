import json
from collections import Counter

with open('barcelona_result.json') as json_data:
    data = json.load(json_data)

# convertir numeros a enters
votes_party_all = [(e["name"], int(e["votes"].replace(".", ""))) for e in data]

total_votes = sum (e[1] for e in votes_party_all)

# eliminar aquells que no arriben al 3%. Si els vots en blanc superessin el 3% s'haurien de treure de la llista (no són un partit)
votes_party = [e for e in votes_party_all if e[1] / total_votes >= 0.03]

# dividir els vots de cada partit per 1, 2, 3, ... 85 (on 85 és el nombre d'escons de la demarcació)
votes_div_escons = [ (e[0], e[1]/i) for i in range(1,86) for e in votes_party]

def getKey(item):
    return item[1]

# ordenar de major a menor
votes_div_escons.sort(key=getKey, reverse=True)

# agafar els 85 (nombre d'escons de la demarcació) primers. Només agafem el nom del partit
escons = [e[0] for e in votes_div_escons[0:85]]

# agrupar i contar
result = Counter(escons)

print("**************")
print(result)

