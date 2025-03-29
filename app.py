from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "API de Gerenciamento de Refeições - MVP"

if __name__ == "__main__":
    app.run(debug=True)