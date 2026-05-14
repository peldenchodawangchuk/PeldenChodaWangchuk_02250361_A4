from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head><title>My DevOps App</title></head>
    <body style="font-family: Arial; text-align: center; padding: 50px;">
        <h1>Hello DevOps!</h1>
        <p>This app is deployed using GitHub Actions and Render.</p>
        <p><em>Assignment IV – DSO101 | SWE</em></p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run()