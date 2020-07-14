import os
import json
import util
import drinks_service

JSON_FILE_PATH = 'data/coktails.json'

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

def serve(uuid):
    command_line = 'python3 ../cli/barbox.py'
    coktail = get(uuid)
    for drink_dose in coktail['drinks']:
        drink = drinks_service.get(drink_dose['uuid'])
        # TODO: Check if the drink volume is available for the coktail.

        # refresh the available volume of the served drinks
        drink['volume_left'] -= drink_dose['volume']
        drinks_service.modify(drink['uuid'], drink)
        duration = util.get_valve_opening_duration(drink_dose['volume'])
        command_line += ' --pump %s %s' % (drink['pump_number'], duration)
    os.system(command_line)