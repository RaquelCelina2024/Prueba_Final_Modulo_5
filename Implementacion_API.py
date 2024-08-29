from flask import Flask, request, jsonify

app = Flask(_name_)

# Base de datos simulada
locations = []

@app.route('/locations', methods=['GET'])
def get_locations():
    return jsonify(locations), 200

@app.route('/locations', methods=['POST'])
def add_location():
    new_location = request.json
    locations.append(new_location)
    return jsonify(new_location), 201

@app.route('/locations/<int:id>', methods=['GET'])
def get_location(id):
    location = next((loc for loc in locations if loc['id'] == id), None)
    if location:
        return jsonify(location), 200
    else:
        return jsonify({"error": "Location not found"}), 404

@app.route('/locations/<int:id>', methods=['PUT'])
def update_location(id):
    location = next((loc for loc in locations if loc['id'] == id), None)
    if location:
        updated_data = request.json
        location.update(updated_data)
        return jsonify(location), 200
    else:
        return jsonify({"error": "Location not found"}), 404

@app.route('/locations/<int:id>', methods=['DELETE'])
def delete_location(id):
    global locations
    locations = [loc for loc in locations if loc['id'] != id]
    return '', 204

if _name_ == '_main_':
    app.run(debug=True)