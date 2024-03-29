from flask import Flask, render_template
app = Flask(__name__, static_folder='../client/dist/static', template_folder='../client/dist')

@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)