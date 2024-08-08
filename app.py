from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/store_data', methods=['POST'])
def store_data():
    return "Store data endpoint"

@app.route('/retrieve_data', methods=['GET'])
def retrieve_data():
    return "Retrieve data endpoint"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
