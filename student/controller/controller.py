
from flask import Blueprint, request, jsonify
import contract.contract as contract

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data['name']
    password = data['password']
    receipt = contract.create_account(name,password)
    return jsonify(receipt)

@bp.route('/login', methods=['POST'])
def login():
    data = request.json
    name = data['name']
    password = data['password']
    receipt = contract.login_account(name,password)
    return jsonify(receipt)

@bp.route('/set-handler', methods=['POST'])
def set_handler():
    data = request.json
    token = request.headers.get('token')
    address = data['address']
    receipt = contract.set_handler(address,token)
    return jsonify(receipt)

@bp.route('/add-student', methods=['POST'])
def add_student():
    data = request.json
    token = request.headers.get('token')
    id = data['id']
    name = data['name']
    receipt = contract.add_student(id,name,token)
    return jsonify(receipt)

@bp.route('/delete-student', methods=['POST'])
def delete_student():
    data = request.json
    id = data['id']
    token = request.headers.get('token')
    receipt = contract.delete_student(id,token)
    return jsonify(receipt)

@bp.route('/add-score', methods=['POST'])
def add_score():
    data = request.json
    token = request.headers.get('token')
    id = data['id']
    subject = data['subject']
    score = data['score']
    receipt = contract.add_student_score(id,subject,score,token)
    return jsonify(receipt)

@bp.route('/update-score', methods=['POST'])
def update_score():
    token = request.headers.get('token')
    data = request.json
    id = data['id']
    num = data['num']
    score = data['score']
    receipt = contract.update_student_score(id,num,score,token)
    return jsonify(receipt)

@bp.route('/get-student', methods=['GET'])
def get_student_info():
    token = request.headers.get('token')
    data = request.json
    id = data['id']
    receipt = contract.get_student_info(id,token)
    return jsonify(receipt)

@bp.route('/get-student-score', methods=['GET'])
def get_student_score():
    token = request.headers.get('token')
    data = request.json
    id = data['id']
    receipt = contract.get(id,token)
    return jsonify(receipt)

@bp.route('/admin', methods=['GET'])
def get_admin():
    receipt = contract.get_admin()
    return jsonify(receipt)