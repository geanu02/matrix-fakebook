from flask import render_template, g


from . import bp
from app import app
from app.forms import UserSearchForm

@app.before_request
def before_request():
    g.user_search_form = UserSearchForm()

@bp.route('/')
def home():
    matrix = {
        'instructors': ('Sean', 'Dylan'),
        'students': ['Ray', 'Hamed', 'Gian', 'Ben', 'Christopher', 'Alec']
    }
    return render_template(
        'index.jinja', 
        title="Matrix Fakebook Homepage", 
        instructors=matrix['instructors'],
        students=matrix['students'],
        user_search_form=g.user_search_form
    )

@bp.route('/about')
def about():
    
    return render_template(
        'about.jinja',
        title="Matrix Fakebook: About Page",
        user_search_form=g.user_search_form
    )