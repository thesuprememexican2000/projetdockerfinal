from flask import Blueprint, jsonify
from .controllers.mysql_controller import get_qtc_tax, get_ctc_tax

mysql_blueprint = Blueprint('mysql', __name__)

@mysql_blueprint.route('/qtc/tax', methods=['GET'])
def get_qtc_tax_route():
    try:
        qtc_tax_info = get_qtc_tax()
        return jsonify(qtc_tax_info)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@mysql_blueprint.route('/ctc/tax', methods=['GET'])
def get_ctc_tax_route():
    try:
        ctc_tax_info = get_ctc_tax()
        return jsonify(ctc_tax_info)
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Internal Server Error