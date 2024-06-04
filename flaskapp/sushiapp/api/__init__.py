from flask import Blueprint
from .order import bp as bp_api_order

bp = Blueprint('api', __name__, url_prefix='/api')

bp.register_blueprint(bp_api_order)
