from flask import Flask, request, jsonify
from caesar_cipher import caesar_cipher_encrypt, caesar_cipher_decrypt

app = Flask(__name__)

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.get_json()
    message = data['message']
    key = int(data['key'])
    encrypted_message = caesar_cipher_encrypt(message, key)
    return jsonify({'encrypted_message': encrypted_message})

@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.get_json()
    message = data['message']
    key = int(data['key'])
    decrypted_message = caesar_cipher_decrypt(message, key)
    return jsonify({'decrypted_message': decrypted_message})

if __name__ == '__main__':
    app.run(debug=True)
