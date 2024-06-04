from flask import Blueprint, request, session, jsonify

bp = Blueprint('api_order', __name__, url_prefix='/order')

@bp.route('/')
def getItems():
	if 'cart' in session:
		return jsonify(session['cart']), 200
	return jsonify({}), 200

@bp.route('/add', methods=['POST'])
def addItem():
	cart = {}
	if 'cart' in session:
		cart = session['cart']
		session.pop('cart', None)
	item_id = request.json['id']
	if item_id not in cart:
		cart[item_id] = 0
	cart[item_id] += 1
	session['cart'] = cart
	return '', 200

@bp.route('/remove', methods=['POST'])
def removeItem():
	cart = {}
	if 'cart' in session:
		cart = session['cart']
		session.pop('cart', None)
	item_id = request.json['id']
	if item_id not in cart:
		return '', 200
	cart[item_id] -= 1
	if cart[item_id] == 0:
		cart.pop(item_id)
	session['cart'] = cart
	return '', 200

@bp.route('/total')
def getTotalItems():
	if 'cart' not in session:
		return jsonify(total=0), 200
	total = sum([session['cart'][key] for key in session['cart']])	
	return jsonify(total=total), 200
