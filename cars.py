from flask import Flask, request, make_response, jsonify

CARS = [
    {'id': 1,
     'car_brand': ' Volswagen',
     'production_year': '1995',
     'Fuel_type': 'gas',
     'car_milage': '20000',
     'registration_number': 'ABC234'
     },
    {'id': 2,
     'car_brand': ' BMW',
     'production_year': '2012',
     'Fuel_type': 'petrol',
     'car_milage': '3000',
     'registration_number': 'DEF567'
     },
    {'id': 3,
     'car_brand': ' Toyota',
     'production_year': '2018',
     'Fuel_type': 'gas',
     'car_milage': '350000',
     'registration_number': 'GHJ890'
     }
]
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def items():
    response_data = {
        'success': True,
        'data': []
    }
    if request.method == 'GET':
        response_data['data'] = CARS
        return jsonify(response_data)
    elif request.method == 'POST':
        data = request.json
        if 'id' not in data or 'car_brand' not in data or 'production_year' not in data or 'Fuel_type' not in data or 'car_milage' not in data:
            response_data['success'] = False
            response = jsonify(response_data)
            response.status_code = 400
            response_data['success'] = False
            response_data['error'] = 'Please provide all required information'
            response = jsonify(response_data)
            response.status_code = 400
        else:
            CARS.append(data)
            response_data['data'] = CARS
            response = jsonify(response_data)
            response.status_code = 201
            return response


@app.route('/cars/<int:car_id>')
def item(car_id):
    response_data = {
        'success': True,
        'data': []
    }
    try:
        item = [element for element in CARS if element['id'] == car_id][0]
    except IndexError:
        response_data['success'] = False
        response = jsonify(response_data)
        response.status_code = 404
    else:
        response_data['data'] = item
        response = jsonify(response_data)
    return response



if __name__ == '__main__':
    app.run(debug=True)
