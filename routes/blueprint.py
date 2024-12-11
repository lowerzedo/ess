from flask import Blueprint
from controllers.controllers import *

blueprint = Blueprint('blueprint', __name__)


blueprint.route('/update', methods=['PUT'])(update_date_main)
