from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    context = {'title': 'Главная страница'}
    return render_template('index.html', **context)


@app.route('/jackets/')
def dress():
    context = {'title': 'Куртки'}
    return render_template('jackets.html', **context)


@app.route('/pants/')
def shoes():
    context = {'title': 'Брюки'}
    return render_template('pants.html', **context)


@app.route('/shoes/')
def jacket_page():
    context = {'title': 'Обувь'}
    return render_template('shoes.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
