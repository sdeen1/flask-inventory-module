from app import app
from flask import render_template, redirect, flash, request
from app.forms import AddItemForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Home")

@app.route('/add', methods=['GET','POST'])
def add():
    form = AddItemForm()
    if form.validate(): #_on_submit():  #request.method == "POST":
        print("form validated")
        flash('Added Item: {}, Item desciption: {}'.format(form.name.data, form.description.data))
        return redirect('/index')
    return render_template('addItem.html', title="Add Item", form=form)