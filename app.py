from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>¡Hola desde Flask en Azure App Service!</h1>\nProfesor, póngame un 7 😎"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
