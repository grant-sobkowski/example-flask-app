from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return(render_template('index.html'))

if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
    app.run(host='0.0.0.0')