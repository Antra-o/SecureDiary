from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask is working!"

if __name__ == "_main_":
    print("Starting Flask test app...")
    app.run(debug=True)