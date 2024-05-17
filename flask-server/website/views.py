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
    current_day = datetime.now().strftime("%A, %B %d")
    return render_template("home.html", user=current_user, current_day=current_day)


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
        existing_entries_count = Pills.query.filter_by(user_id=session.get('userId')).count()
        if existing_entries_count >= 4:
            return jsonify({'error': 'Maximum number of pills reached.'})
        
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