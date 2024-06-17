from flask import Blueprint, g, request, jsonify
from ..db import uses_database
from ..db.models import MenuItem
from sqlalchemy import select

bp = Blueprint('api_item', __name__, url_prefix='/item')

@uses_database
def menuItems():
	items = []
	if 'db' in g:
		items = [i for i in g.db.scalars(select(MenuItem)).all()]
	return items

@bp.route('/')
def getMenuItems():
	items = [{"name": i.name, "price": i.price} for i in menuItems()]
	return jsonify(items), 200

@bp.route('/new', methods=['POST'])
@uses_database
def newMenuItem():
	name = request.json['name']
	if len(name) > 100:
		return 'Error: Name too long', 400
	error = False
	try: 
		price = int(request.json['price'])
	except ValueError:
		error = True
	if error or str(price) != request.json['price']:
		return 'Error: Invalid price', 400
	newItem = MenuItem(name=name, price=price)
	g.db.add(newItem)
	return '', 200