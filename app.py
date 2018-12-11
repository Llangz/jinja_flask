from flask import Flask, render_template, request
from mysql.connector import connect

app = Flask(__name__)
db = connect(host='localhost', user='root', passwd='', database='uchumi')

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/products')
def products():
    return render_template('products.html')


@app.route('/add', methods=["POST", "GET"])
def add():
    if request.method == "GET":
        return render_template('add_products.html')
    else:
        print(request.form)
        name = request.form["name"]
        quantity = request.form["quantity"]
        price = request.form["price"]
        cursor = db.cursor()
        sql = "insert into products values(null, %s, %s, %s)"
        data = (name, quantity, price)
        cursor.execute(sql, data)
        db.commit()

        print(name, quantity, price)

    return render_template('add_products.html')


if __name__ == '__main__':
    app.run(debug=True)

#  create a form with   name of the product, quantity, unit price, extend and create a new route called /add
