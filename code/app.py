from flask import Flask

app = Flask(__name__)
app.secret_key = "super secret key"

@app.route('/')
@app.route('/index')
def index():
    pass

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)