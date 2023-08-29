from app import app, db
from flask import render_template, redirect, flash, request, url_for
from app.forms import AddItemForm
from app.models import Item

@app.route('/')
@app.route('/index')
def index():
    items = Item.query.all()
    return render_template('index.html', title="Home", items=items)

@app.route('/add', methods=['GET','POST'])
def add():
    form = AddItemForm()
    if form.validate(): #_on_submit():  #request.method == "POST":
        item = Item(
            name = form.name.data,
            description = form.description.data,
            total = form.total.data,
            available = form.total.data,
            halfDay = form.halfDay.data,
            day = form.day.data,
            week = form.week.data,
            month = form.month.data
        )
        db.session.add(item)
        db.session.commit()
        print("form validated")
        flash('Added Item: {}, Item desciption: {}'.format(form.name.data, form.description.data))
        return redirect(url_for('index'))
    return render_template('addItem.html', title="Add Item", form=form)

@app.route('/update/<id>', methods=['GET','POST'])
def update(id):
    item = db.get_or_404(Item, id)
    form = AddItemForm(obj=item)
    if form.validate(): #_on_submit():  #request.method == "POST":
        item.name = form.name.data
        item.description = form.description.data
        item.total = form.total.data
        item.halfDay = form.halfDay.data
        item.day = form.day.data
        item.week = form.week.data
        item.month = form.month.data
        # Update the database
        #db.session.add(item)
        db.session.commit()
        print("form validated")
        print('Updated Item: {}, Item desciption: {}'.format(form.name.data, form.description.data))
        return redirect(url_for('index'))
    return render_template('addItem.html', title='Update Item', form=form)

@app.route('/delete/<id>')
def delete(id):
    item = db.get_or_404(Item, id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/rent/<id>')
def rent(id):
    item = db.get_or_404(Item, id)
    if item.available is not None:
        item.available = max(0, int(item.available) - 1)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/return/<id>')
def return_item(id):
    item = db.get_or_404(Item, id)
    if item.available is not None:
        item.available = min(int(item.total), int(item.available) + 1)
        db.session.commit()
    return redirect(url_for('index'))