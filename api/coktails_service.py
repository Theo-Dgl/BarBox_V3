import os
import json
import util
import drinks_service

JSON_FILE_PATH = 'data/coktails.json'

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
        file.seek(0)
        file.truncate()
        new_drink['id'] = util.get_uuid()
        data.append(new_drink)
        json.dump(data, file)
        return True

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
        return True

def serve(id):
    command_line = 'python3 ../cli/barbox.py'
    coktail = get(id)
    for drink_dose in coktail['drinks']:
        drink = drinks_service.get(drink_dose['id'])
        # TODO: Check if the drink volume is available for the coktail.

        # refresh the available volume of the served drinks
        drink['volume_left'] -= drink_dose['volume']
        drinks_service.modify(drink['id'], drink)
        duration = util.get_valve_opening_duration(drink_dose['volume'])
        command_line += ' --pump %s %s' % (drink['pump_number'], duration)
    os.system(command_line)