from flask import render_template

from . import bp

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
        students=matrix['students']
    )

@bp.route('/about')
def about():
    
    return render_template(
        'about.jinja',
        title="Matrix Fakebook: About Page"
    )