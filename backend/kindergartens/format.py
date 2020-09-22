import json

jsondata = []
with open('kindergartens/data2.json', 'r') as json_file:
    kindergartens =  json.load(json_file)

for kindergarten in kindergartens:
    temp = {}
    temp['model'] = 'kindergartens.kindergarten'
    field = {}
    for key, value in kindergarten.items():
        if key == 'after-school_inclusion':
            key = 'after_school_inclusion'
        if (key == 'lat' or key == 'lng') and kindergarten[key] == '':
            continue
        if key == 'lat' or key == 'lng':
            value = float(value)
        field[key] = value
        temp['fields'] = field
    jsondata.append(temp)

with open('data.json', 'w', encoding="UTF-8") as make_file:
    json.dump(jsondata, make_file, indent="\t")