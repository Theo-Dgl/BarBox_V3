import json
import util

JSON_FILE_PATH = 'data/drinks.json'

def list():
    with open(JSON_FILE_PATH) as json_file:
        data = json.load(json_file)
        return data

def get(id):
    with open(JSON_FILE_PATH) as json_file:
        data = json.load(json_file)
        for drink in data:
            if drink['id'] == id: return drink
        return None

def add(new_drink):
    with open(JSON_FILE_PATH, "r+") as file:
        data = json.load(file)
        for drink in data:
            if drink['pump_number'] == new_drink['pump_number'] : return False
        file.seek(0)
        file.truncate()
        new_drink['id'] = util.get_uuid()
        data.append(new_drink)
        json.dump(data, file)
        for drink in data:
            if drink['id'] == new_drink['id']: return drink

def delete(id):
    with open(JSON_FILE_PATH, "r+") as file:
        data = json.load(file)
        for index, drink in enumerate(data):
            if drink['id'] == id : del data[index]
        file.seek(0)
        file.truncate()
        json.dump(data, file)
        return True

def modify(id, new_value):
    with open(JSON_FILE_PATH, "r+") as file:
        data = json.load(file)
        for index, drink in enumerate(data):
            if drink['id'] == id : 
                for new_val in new_value.keys():
                    print(new_val)
                    data[index][new_val] = new_value[new_val]
        file.seek(0)
        file.truncate()
        json.dump(data, file)
        for drink in data:
            if drink['id'] == id: return drink