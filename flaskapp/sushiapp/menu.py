from flask import Blueprint, render_template, g, current_app
from .tabs import tabs
from .db.models import MenuItem

items = [
	MenuItem(name='Maki', price=100),
	MenuItem(name='Nigiri', price=200),
	MenuItem(name='Temaki', price=300)
]

bp = Blueprint('menu', __name__, url_prefix='/menu')

@bp.route('/')
def menu():
	return render_template('menu.html', items=items, tabs=tabs)
