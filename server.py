from flask import Flask, jsonify, request
from werkzeug.serving import run_simple

app = Flask(__name__)

drivers = [
        {
        "id": 1,
        "name":"Aidan Williams",
        "phone":"(980) 867-1653",
        "address":"1210 Tomko Rd."
    },
    {
        "id": 2,
        "name":"Alec Boron",
        "phone":"(240) 586-4753",
        "address":"1626 Patrick Henry Drive Apartment 144"
    },
]

@app.route('/drivers', methods=['GET'])
def get_drivers():
    sorted_drivers = sorted(drivers, key=lambda k: k['name'])
    drivers_formatted = [{'Name': driver['name'], 'Address': driver['address'], 'Phone Number': driver['phone']} for driver in sorted_drivers]
    return jsonify(drivers_formatted)

@app.route('/drivers', methods=['POST'])
def add_driver():
    driver = request.get_json()
    drivers.append(driver)
    return '', 204

@app.route('/drivers/<int:driver_id>', methods=['DELETE'])
def remove_driver(driver_id):
    if driver_id >= len(drivers):
        return 'Driver not found', 404
    drivers.pop(driver_id)
    return '', 204

@app.route('/drivers/<int:driver_id>', methods=['PUT'])
def update_driver(driver_id):
    if driver_id >= len(drivers):
        return 'Driver not found', 404
    driver = request.get_json()
    drivers[driver_id].update(driver)
    return '', 204

if __name__ == '__main__':
    run_simple('localhost', 8000, app, use_reloader=True, use_debugger=True)
