from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'World')
    return jsonify({"message": f"Hello, {name}!"})

if __name__ == "__main__":
    app.run(debug=True)
