
from flask import Blueprint, request, jsonify
import contract.contract as contract

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/set-handler', methods=['POST'])
def set_handler():
    data = request.json
    address = data['address']
    receipt = contract.set_handler(address)
    return jsonify(receipt)

@bp.route('/add-student', methods=['POST'])
def set_handler():
    data = request.json
    id = data['id']
    name = data['name']
    receipt = contract.set_handler(id,name)
    return jsonify(receipt)

@bp.route('/delete-student', methods=['POST'])
def delete_student():
    data = request.json
    id = data['id']
    receipt = contract.delete_student(id)
    return jsonify(receipt)

@bp.route('/add-score', methods=['POST'])
def add_score():
    data = request.json
    id = data['id']
    subject = data['subject']
    score = data['score']
    receipt = contract.add_student_score(id,subject,score)
    return jsonify(receipt)

@bp.route('/update-score', methods=['POST'])
def add_score():
    data = request.json
    id = data['id']
    num = data['num']
    score = data['score']
    receipt = contract.update_student_score(id,num,score)
    return jsonify(receipt)

@bp.route('/get-student', methods=['GET'])
def add_score():
    data = request.json
    id = data['id']
    receipt = contract.get_student_info(id)
    return jsonify(receipt)

@bp.route('/admin', methods=['GET'])
def get_admin():
    receipt = contract.get_admin()
    return jsonify(receipt)