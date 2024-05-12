from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Pill
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        pill = request.form.get('pill') # Gets the pill from the HTML 

        if len(pill) < 1:
            flash('Pill is too short!', category='error') 
        else:
            new_pill = Pill(data=pill, user_id=current_user.id)  #providing the schema for the pill 
            db.session.add(new_pill) # adding the pill to the database 
            db.session.commit()
            flash('Pill added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-pill', methods=['POST'])
def delete_pill():  
    pill = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    pillId = pill['pillId']
    pill = Pill.query.get(pillId)
    if pill:
        if pill.user_id == current_user.id:
            db.session.delete(pill)
            db.session.commit()

    return jsonify({})