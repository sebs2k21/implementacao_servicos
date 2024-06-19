# Sebastian Fabian Pires do Carmo 2120283
# Implementação de serviços

from flask import Flask, jsonify, request

app = Flask(__name__)

# Conversão de temperatura de Celsius para Fahrenheit
@app.route('/convert/celsius_to_fahrenheit', methods=['GET'])
def celsius_to_fahrenheit():
    celsius = request.args.get('celsius', type=float)
    if celsius is None:
        return jsonify({'error': 'Invalid or missing parameter: celsius'}), 400
    fahrenheit = (celsius * 9/5) + 32
    return jsonify({'celsius': celsius, 'fahrenheit': fahrenheit})

# Conversão de temperatura de Celsius para Kelvin
@app.route('/convert/celsius_to_kelvin', methods=['GET'])
def celsius_to_kelvin():
    celsius = request.args.get('celsius', type=float)
    if celsius is None:
        return jsonify({'error': 'Invalid or missing parameter: celsius'}), 400
    kelvin = celsius + 273.15
    return jsonify({'celsius': celsius, 'kelvin': kelvin})

# Conversão de Dólar para Real
@app.route('/convert/usd_to_brl', methods=['GET'])
def usd_to_brl():
    usd = request.args.get('usd', type=float)
    if usd is None:
        return jsonify({'error': 'Invalid or missing parameter: usd'}), 400
    brl = usd * 5.5
    return jsonify({'usd': usd, 'brl': brl})

# Conversão de Euro para Real
@app.route('/convert/eur_to_brl', methods=['GET'])
def eur_to_brl():
    eur = request.args.get('eur', type=float)
    if eur is None:
        return jsonify({'error': 'Invalid or missing parameter: eur'}), 400
    brl = eur * 5.9
    return jsonify({'eur': eur, 'brl': brl})

if __name__ == '__main__':
    app.run(debug=True)


# Url para teste
# http://127.0.0.1:5000/convert/celsius_to_fahrenheit?celsius=100
# http://127.0.0.1:5000/convert/celsius_to_kelvin?celsius=100
# http://127.0.0.1:5000/convert/usd_to_brl?usd=10
# http://127.0.0.1:5000/convert/eur_to_brl?eur=10