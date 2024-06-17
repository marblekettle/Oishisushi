from flask import Blueprint, render_template, g, current_app
from .tabs import tabs
from .db.models import MenuItem
from .api.item import menuItems
import json

items = []

bp = Blueprint('menu', __name__, url_prefix='/menu')

@bp.route('/')
def menu():
	items = menuItems()
	return render_template('menu.html', items=items, tabs=tabs)
