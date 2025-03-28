from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify(message="Welcome to the Flask API! Phillip Knezevich")

@app.route('/hello', methods=['GET'])
def hello():
    name = request.args.get('name', 'World')
    return jsonify(greeting=f"Hello, {name}!")

# if __name__ == '__main__':
#     app.run(debug=True)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
