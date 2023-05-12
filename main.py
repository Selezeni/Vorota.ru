from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html', title='Главная')


@app.route("/info")
def info():
    return render_template('info.html', title='Информация')


@app.route("/vorota")
def vorota():
    return render_template('vorota.html', title='Ворота')


@app.route("/rolets")
def rolets():
    return render_template('rolets.html', title='Рольставни')


@app.route("/barrier")
def barrier():
    return render_template('barrier.html', title='Шлагбаумы')


@app.route("/catalog")
def catalog():
    return render_template('catalog.html', title='Каталог')


if __name__ == '__main__':
    app.run(debug=True)
