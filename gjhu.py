import  json


data = {"каша": 90,
        "бутерброд": 50,
        "чай": 20}


def save():
    with open('blbl.json', 'w',encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

save()