from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/products')
def products():
    items = ["Unga", "Kitchenware", "LivingRoom", "Decor", "Backyard"]
    return render_template('products.html', items=items)


@app.route('/contact')
def contact():
    media = ["Email", "Twitter", "Facebook", "Instagram"]
    return render_template('contact.html', media=media)


if __name__ == '__main__':
    app.run(debug=True)










#  create a form with   name of the product, quantity, unit price, extend and create a new route called /add
