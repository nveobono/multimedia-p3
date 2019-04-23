from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/articulo1')
def articulo1():
    return render_template('articulo1.html')

@app.route('/articulo2')
def articulo2():
    return render_template('articulo2.html')

@app.route('/articulo3')
def articulo3():
    return render_template('articulo3.html')

if __name__ == '__main__':
    app.run(debug= True)