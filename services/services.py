import datetime
from flask import request, jsonify
from queries.queries import update_values, update_values_i
from helpers.validations import UpdateDateSchema

# route: */ess/update
def update_date(**kwargs):
    # column is a string
    column = request.json.get('column')
    # nno is a list of integers
    nno = request.json.get('nno')
    # date is a string in the format 'dd-mm-yyyy'
    date = request.json.get('date')
    date = datetime.strptime(date, '%d-%m-%Y') if date else "NULL"

    if not column or not nno:
        return jsonify({'error': 'Bad Request'}), 400

    if column not in ['Script2_ReceiveDate', 'Script2_DueDate', 'Script_DueDate', 'Script_ReceiveDate']:
        return jsonify({'error': 'Invalid column'}), 400

    # validate 
    try:
        UpdateDateSchema().load({"column": column, "nno": nno, "date": date})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
    # try:
    update_values({"column": column, "nno": nno, "date": date})
    update_values_i({"column": column, "nno": nno, "date": date})
    # except Exception as e:
        # return jsonify({'error': str(e)}), 500

    return jsonify({'message': 'Updated successfully'}), 200
