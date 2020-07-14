import uuid
import math

# each pump can provide 2cl / second
PUMP_FLOW = 2

def get_uuid():
    return str(uuid.uuid4())

def get_valve_opening_duration(required_volume):
    return round(required_volume/PUMP_FLOW)