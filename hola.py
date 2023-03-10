# Creacion del flask
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    title = "Control de proyectos"
    user = {'nombre': 'Alvaro'}

    return render_template('index.html', title=title, user=user)

if __name__ == "__main__":
    app.run(debug=True, port=5000)