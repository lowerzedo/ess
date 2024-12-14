from datetime import datetime
from flask import request, jsonify
from queries.queries import update_values, update_values_i
from helpers.validations import UpdateDateSchema

# route: */ess/update
def update_date(**kwargs):
    column = request.json.get('column')
    nno_raw = request.json.get('nno')
    # date is a string in the format 'dd-mm-yyyy'
    date_str = request.json.get('date')
    date = datetime.strptime(date_str, '%d-%m-%Y') if date_str else None


    if not column or not nno_raw:
        return jsonify({'error': 'Bad Request'}), 400

    if column not in ['Script2_ReceiveDate', 'Script2_DueDate', 'Script_DueDate', 'Script_ReceiveDate']:
        return jsonify({'error': 'Invalid column'}), 400

    # validate 
    try:
        UpdateDateSchema().load({"column": column, "nno": nno_raw, "date": date_str})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    

    # Convert string to list of integers
    nno = [int(x.strip()) for x in nno_raw.split(',')] if isinstance(nno_raw, str) else nno_raw


    # try:
    update_values({"column": column, "nno": nno, "date": date})
    update_values_i({"column": column, "nno": nno, "date": date})
    # except Exception as e:
        # return jsonify({'error': str(e)}), 500

    return jsonify({'message': 'Updated successfully'}), 200
