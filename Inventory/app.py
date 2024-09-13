from flask import Flask, render_template, request, redirect, url_for
from models import db, CarDue
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()  # Ensures that the database tables are created before handling any requests

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/part_due', methods=['GET', 'POST'])
def part_due():
    if request.method == 'POST':
        reg_no = request.form['reg_no']
        model_name = request.form['model_name']
        part_required = request.form['part_required']
        date_time = datetime.now()
        dealership = request.form['dealership']

        new_due = CarDue(reg_no=reg_no, model_name=model_name, part_required=part_required, date_time=date_time, dealership=dealership)
        db.session.add(new_due)
        db.session.commit()

        return redirect(url_for('active_dues'))

    return render_template('part_due.html')

@app.route('/active_dues', methods=['GET', 'POST'])
def active_dues():
    dues = CarDue.query.all()
    if request.method == 'POST':
        reg_no = request.form['reg_no']
        due = CarDue.query.filter_by(reg_no=reg_no).first()
        db.session.delete(due)
        db.session.commit()
        return redirect(url_for('active_dues'))

    return render_template('active_dues.html', dues=dues)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
