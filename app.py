from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/sumar', methods=['POST'])
def sumar():
    data = request.json
    a = data.get('a', 0)
    b = data.get('b', 0)

    try:
        resultado = float(a) + float(b)
    except (ValueError, TypeError):
        return jsonify({'error': 'Los valores deben ser números'}), 400
    return jsonify({'resultado': resultado})
