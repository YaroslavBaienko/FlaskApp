from flask import (
    Flask,
    request,
    make_response,
    abort,
    render_template
)

app = Flask(__name__)
app.static_folder = 'static'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/process')
def process():
    return render_template('process.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/calc', methods=['GET', 'POST'])
def calc():
    if request.method == "POST":
        distance = float(request.form['distance'])
        time = float(request.form['time'])
        speed = round((distance / time), 3)

        return render_template('speed.html', distance=distance, time=time, speed=speed)
    return render_template('calc.html')


if __name__ == '__main__':
    app.run()
