from flask import Flask, abort, jsonify, make_response, request
import drinks_service
import coktails_service

app = Flask(__name__)

# ERROR PART
@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# DRINKS ENDPOINT
@app.route('/drinks', methods=['GET'])
def list_drinks():
    dictionnaire = drinks_service.list()
    return jsonify(dictionnaire)

@app.route('/drinks/<string:uuid>', methods=['GET'])
def get_drink(uuid):
    dictionnaire = drinks_service.get(uuid)
    if dictionnaire == None:
        abort(404)
    return jsonify(dictionnaire)

@app.route('/drinks', methods=['POST'])
def add_drink():
    if not request.json or not 'pump_number' in request.json or not 'name' in request.json or not 'total_volume' in request.json:
        abort(400)
    drinks_service.add(request.json)
    return make_response(jsonify({}), 204)

@app.route('/drinks/<string:uuid>', methods=['PUT'])
def modify_drink(uuid):
    if not request.json:
        abort(400)
    dictionnaire = drinks_service.get(uuid)
    if dictionnaire == None:
        abort(404)
    drinks_service.modify(uuid, request.json)
    return make_response(jsonify({}), 204)

@app.route('/drinks/<string:uuid>', methods=['DELETE'])
def remove_drink(uuid):
    dictionnaire = drinks_service.get(uuid)
    if dictionnaire == None:
        abort(404)
    drinks_service.delete(uuid)
    return make_response(jsonify({}), 204)

# COKTAILS ENDPOINT
@app.route('/coktails', methods=['GET'])
def list_coktails():
    dictionnaire = coktails_service.list()
    return jsonify(dictionnaire)

@app.route('/coktails/<string:uuid>', methods=['GET'])
def get_coktail(uuid):
    dictionnaire = coktails_service.get(uuid)
    if dictionnaire == None:
        abort(404)
    return jsonify(dictionnaire)

@app.route('/coktails/<string:uuid>/serve', methods=['POST'])
def serve_coktail(uuid):
    dictionnaire = coktails_service.get(uuid)
    if dictionnaire == None:
        abort(404)
    coktails_service.serve(uuid)    
    return make_response(jsonify({}), 204)

@app.route('/coktails', methods=['POST'])
def add_coktail():
    if not request.json or not 'drinks' in request.json or not 'name' in request.json or not 'image' in request.json:
        abort(400)
    coktails_service.add(request.json)
    return make_response(jsonify({}), 204)

# Main entrypoint
if __name__ == '__main__':
    app.run(debug=True)