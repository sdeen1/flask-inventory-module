from app import app
from flask import render_template
from app.forms import AddItemForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Home")

@app.route('/add', methods=['GET','POST'])
def add():
    form = AddItemForm()
    return render_template('addItem.html', title="Add Item", form=form)