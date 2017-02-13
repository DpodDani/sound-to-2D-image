from flask import Flask, render_template, request
import imp
app = Flask(__name__)

test = imp.load_source('main', './static/test.py')

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/test", methods=['GET', 'POST'])
def testing():
    print("Something is working :D")
    return test.confirmMessage()

@app.route("/colourSound", methods=['POST'])
def getColourSound():
    buttonColour = request.form['buttonColour']
    print("Pressed " + buttonColour + " button")
    print test.confirmColour(buttonColour)
    return "Played sound"

if __name__ == "__main__":
    app.run()
