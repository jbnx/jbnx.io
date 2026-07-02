import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # This is the HTML text that will be displayed on your website
    return "<h1>CipherDeck // Hello World!</h1>"

if __name__ == '__main__':
    # Railway assigns a dynamic port, so we must fetch it from the environment
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
