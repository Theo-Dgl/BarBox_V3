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
    drinks = drinks_service.list()
    return jsonify({'data':drinks})

@app.route('/drinks/<string:id>', methods=['GET'])
def get_drink(id):
    drink = drinks_service.get(id)
    if drink == None:
        abort(404)
    return jsonify({'data': drink})

@app.route('/drinks', methods=['POST'])
def add_drink():
    if not request.json or not 'pump_number' in request.json or not 'name' in request.json or not 'total_volume' in request.json:
        abort(400)
    drink = drinks_service.add(request.json)
    return make_response(jsonify(drink), 200)

@app.route('/drinks/<string:id>', methods=['PUT'])
def modify_drink(id):
    if not request.json:
        abort(400)
    drink = drinks_service.get(id)
    if drink == None:
        abort(404)
    drink = drinks_service.modify(id, request.json)
    return make_response(jsonify(drink), 200)

@app.route('/drinks/<string:id>', methods=['DELETE'])
def remove_drink(id):
    dictionnaire = drinks_service.get(id)
    if dictionnaire == None:
        abort(404)
    drinks_service.delete(id)
    return make_response(jsonify({}), 204)

# COKTAILS ENDPOINTS
@app.route('/coktails', methods=['GET'])
def list_coktails():
    coktails = coktails_service.list()
    return jsonify({'data':coktails})

@app.route('/coktails/<string:id>', methods=['GET'])
def get_coktail(id):
    coktail = coktails_service.get(id)
    if coktail == None:
        abort(404)
    return jsonify({'data':coktail})

@app.route('/coktails/<string:id>', methods=['PUT'])
def modify_coktail(id):
    if not request.json:
        abort(400)
    coktail = coktails_service.get(id)
    if coktail == None:
        abort(404)
    coktail = coktails_service.modify(id, request.json)
    return make_response(jsonify(coktail), 200)

@app.route('/coktails/<string:id>/serve', methods=['POST'])
def serve_coktail(id):
    dictionnaire = coktails_service.get(id)
    if dictionnaire == None:
        abort(404)
    coktails_service.serve(id)    
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