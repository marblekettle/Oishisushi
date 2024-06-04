from flask import Blueprint, render_template, url_for, send_file
from .tabs import tabs

bp = Blueprint('home', __name__)

@bp.route('/')
def home():
	return render_template('home.html', tabs=tabs)

@bp.route('/favicon.ico')
def favicon():
	return send_file('./static/favicon.ico', 'image/ico')
