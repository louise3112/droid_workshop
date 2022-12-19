from flask import Flask, render_template
from controllers.technicians_controller import technicians_blueprint
from controllers.droids_controller import droids_blueprint

app = Flask(__name__)

app.register_blueprint(technicians_blueprint)
app.register_blueprint(droids_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)