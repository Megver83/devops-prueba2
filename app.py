from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>¡Hola desde Flask en Azure App Service!</h1>\nProfesor, póngame un 7 😎"

@app.route("/video")
def video():
    return """
    <html>
      <head><title>Video Embebido</title></head>
      <body style="display: flex; justify-content: center; align-items: center; height: 100vh;">
        <iframe width="560" height="315"
          src="https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ"
          title="YouTube video player"
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen>
        </iframe>
      </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
