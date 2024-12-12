from flask import Flask, jsonify, request
from typing import Optional
from flask_pydantic import validate
from schemas.schemas_greet import GreetRequest
import os

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
@validate(query=GreetRequest)
def greet():
    """
    Greet a user with a message.
    Validate request query parameters and response body.
    """
    name = request.args.get('name')
    if name is None:
        return jsonify({'message': 'Hello, World!'})
    return jsonify({'message': f'Hello, {name}!'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0',port=port)

