from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <head><title>My Page</title></head>
        <body>
            <h1>Hello from Python!</h1>
            <p>This is HTML served by a Python web server.</p>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
