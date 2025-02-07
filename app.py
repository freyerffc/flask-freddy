from flask import Flask, render_template

app = Flask(__name__)

# Ruta Home
@app.route('/')
def home():
    return render_template('index.html')

# Ruta Contacto
@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

# Ruta Acerca de
@app.route('/acerca')
def acerca():
    return render_template('acerca.html')

if __name__ == '__main__':
    app.run(debug=True)
