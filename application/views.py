from flask import Blueprint, render_template
from .models import Sample

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html'), 200

@views.route('/view')
def api_view():
    """
        View page for the Sample API

        Parameters:
        url route

        Returns:
        template and HTTPResponse
    """
    table = Sample.query.all()
    return render_template("view.html", table=table), 200