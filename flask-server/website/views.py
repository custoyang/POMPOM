from flask import Blueprint, render_template, request, flash, jsonify, session
from flask_login import login_required, current_user
from datetime import datetime, time
from .models import Pills
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    # if request.method == 'POST': 
    #     pill = request.form.get('pill') # Gets the pill from the HTML 

    #     if len(pill) < 1:
    #         flash('Pill is too short!', category='error') 
    #     else:
    #         new_pill = Pills(data=pill, user_id=current_user.id)  #providing the schema for the pill 
    #         db.session.add(new_pill) # adding the pill to the database 
    #         db.session.commit()

    return render_template("home.html", user=current_user)


@views.route('/delete-pill', methods=['POST'])
def delete_pill():  
    pill = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    pillId = pill['pillId']
    pill = Pills.query.get(pillId)
    if pill:
        if pill.user_id == current_user.id:
            db.session.delete(pill)
            db.session.commit()

    return jsonify({})

# Route to handle form submission
@views.route('/add_pill', methods=['POST'])
def add_pill():
    if request.method == 'POST':
        data = request.json
        size = data['size']
        amount = data['amount']
        name = data['name']
        alt_name = data['altName']
        dispense_time = datetime.strptime(data['dispenseTime'], '%H:%M').time()
        frequency = data['frequency']
        start_date = datetime.strptime(data['startDate'], '%Y-%m-%d').date()
        end_date = datetime.strptime(data['endDate'], '%Y-%m-%d').date()
        user_id = session.get('userId') # maggie note: modify this to be the same as the user primary key

        # Create a new instance of Pills model
        new_pill = Pills(
            size=size,
            amount=amount,
            name=name,
            alt_name=alt_name,
            dispense_time=dispense_time,
            frequency=frequency,
            start_date=start_date,
            end_date=end_date,
            user_id = user_id
        )

        db.session.add(new_pill)
        db.session.commit()

        print('Pill added successfully')
        
        return jsonify({'message': 'Pill added successfully'})
    else:
        return jsonify({'error': 'Invalid request method'})