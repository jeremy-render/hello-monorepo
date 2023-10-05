from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return f'Hello, World! f{str(dict(request.headers))}'

if __name__ == '__main__':
    print('Hello main!', flush=True)
    app.run(host='0.0.0.0', port=10000, debug=True)