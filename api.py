from flask import Flask, request, jsonify

app = Flask(__name__)

# قائمة المفاتيح الصالحة
valid_keys = ["key1234", "key5678", "keyabcd"]

@app.route('/validate_key', methods=['GET'])
def validate_key():
    authkey = request.args.get('authkey')
    if authkey in valid_keys:
        return jsonify({"message": "Valid key", "status": "success"}), 200
    else:
        return jsonify({"message": "Invalid key", "status": "failure"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
