from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
import requests

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/search')
def search():
    search_query = request.args.get('search_query')
    results = []
    if search_query:
        # Use a string for the API key
        api_key = 'AIzaSyAy9h5zz1UiXzf9FnqiIPg0P0AMk3VGjbw'  
        params = {
            'q': search_query,
            'key': api_key
        }
        # Ensure you use the correct URL for the Google Books API
        response = requests.get('https://www.googleapis.com/books/v1/volumes', params=params)
        
        if response.ok:
            data = response.json()
            results = data.get('items', [])
            # Further processing of results...
        else:
            flash('Error fetching results from Google Books', category='error')
    return render_template("search.html", user=current_user, results=results)



@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})