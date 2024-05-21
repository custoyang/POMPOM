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
    pillId = json.loads(request.data)
    print(pillId)
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
        # Fetch the current user ID from Flask-Login's current_user
        user_id = current_user.id

        # Count only the pills that belong to the current user
        existing_entries_count = Pills.query.filter_by(user_id=user_id).count()
        if existing_entries_count >= 4:
            return jsonify({'error': 'Maximum number of pills reached.'})
        
        data = request.json
        pill_id = data['compartment']
        size = data['size']
        amount = data['amount']
        name = data['name']
        alt_name = data['altName']
        dispense_time = str(datetime.strptime(data['dispenseTime'], '%H:%M').time())
        frequency = data['frequency']
        start_date = datetime.strptime(data['startDate'], '%Y-%m-%d').date()
        end_date = datetime.strptime(data['endDate'], '%Y-%m-%d').date()

        # Create a new instance of Pills model
        new_pill = Pills(
            compartment=pill_id,
            size=size,
            amount=amount,
            name=name,
            alt_name=alt_name,
            dispense_time=dispense_time,
            frequency=frequency,
            start_date=start_date,
            end_date=end_date,
            user_id=user_id  # Use the fetched user ID
        )

        db.session.add(new_pill)
        db.session.commit()

        print('views Pill added successfully')
        
        return jsonify({'message': 'Pill added successfully'})
    else:
        return jsonify({'error': 'Invalid request method'})
    

# Route to handle form submission
@views.route('/update_pill', methods=['POST'])
def update_pill():
    if request.method == 'POST':
        # Fetch the current user ID from Flask-Login's current_user
        user_id = current_user.id
        
        data = request.json
        pill_id = data['compartment']
        pill = Pills.query.filter_by(compartment=pill_id, user_id=user_id).first()

        if pill:
            pill.size = data['size']
            pill.amount = data['amount']
            pill.name = data['name']
            pill.alt_name = data['altName']
            pill.dispense_time = str(datetime.strptime(data['dispenseTime'], '%H:%M').time())
            pill.frequency = data['frequency']
            pill.start_date = datetime.strptime(data['startDate'], '%Y-%m-%d').date()
            pill.end_date = datetime.strptime(data['endDate'], '%Y-%m-%d').date()

            db.session.commit()

        print('Pill updated successfully')
        
        return jsonify({'message': 'Pill updated successfully'})
    else:
        return jsonify({'error': 'Invalid request method'})


@views.route('/get_pill', methods=['GET'])
def get_pill():
    if request.method == 'GET':
        pill_id = request.args.get('id')

        pill = Pills.query.filter_by(id=pill_id).first()

        if pill:
            pill_data = {
                'id': pill.id,
                'size': pill.size,
                'amount': pill.amount,
                'name': pill.name,
                'alt_name': pill.alt_name,
                'dispense_time': pill.dispense_time,
                'frequency': pill.frequency,
                'start_date': pill.start_date.strftime('%Y-%m-%d'),
                'end_date': pill.end_date.strftime('%Y-%m-%d') if pill.end_date else None,
                'user_id': pill.user_id
            }

            print(pill_data)
            return jsonify(pill_data)
        else:
            return jsonify({'error': 'Pill not found'})
    else:
        return jsonify({'error': 'Invalid request method'})