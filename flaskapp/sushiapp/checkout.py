from flask import Blueprint

bp = Blueprint('checkout', __name__, url_prefix='/checkout')

@bp.route('/')
def checkout():
	return render_template('checkout.html')