import json
import util

JSON_FILE_PATH = 'data/drinks.json'

def list():
    with open(JSON_FILE_PATH) as json_file:
        data = json.load(json_file)
        return data

def get(uuid):
    with open(JSON_FILE_PATH) as json_file:
        data = json.load(json_file)
        for drink in data:
            if drink['uuid'] == uuid: return drink
        return None

def add(new_drink):
    with open(JSON_FILE_PATH, "r+") as file:
        data = json.load(file)
        for drink in data:
            if drink['pump_number'] == new_drink['pump_number'] : return False
        file.seek(0)
        file.truncate()
        new_drink['uuid'] = util.get_uuid()
        data.append(new_drink)
        json.dump(data, file)
        return True

def delete(uuid):
    with open(JSON_FILE_PATH, "r+") as file:
        data = json.load(file)
        for index, drink in enumerate(data):
            if drink['uuid'] == uuid : del data[index]
        file.seek(0)
        file.truncate()
        json.dump(data, file)
        return True

def modify(uuid, new_value):
    with open(JSON_FILE_PATH, "r+") as file:
        data = json.load(file)
        for index, drink in enumerate(data):
            if drink['uuid'] == uuid : 
                for new_val in new_value.keys():
                    print(new_val)
                    data[index][new_val] = new_value[new_val]
        file.seek(0)
        file.truncate()
        json.dump(data, file)
        return True
