
from flask import Blueprint, request, jsonify
import contract.contract as contract
import db.db as db
from .response import response

bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data['name']
    password = data['password']
    receipt = contract.create_account(name,password)
    if (receipt == 1) :
        return response(data="error",status_code=0)
    else:
        return response(receipt)


@bp.route('/login', methods=['POST'])
def login():
    data = request.json
    name = data['name']
    password = data['password']
    receipt = contract.login_account(name,password)
    if (receipt == 1):
        return response(data="error", status_code=0)
    else:
        return response(receipt)


@bp.route('/set-handler', methods=['POST'])
def set_handler():
    data = request.json
    token = request.headers.get('token')
    address = data['address']
    receipt = contract.set_handler(address,token)
    if (receipt == 1):
        return response(data="error", status_code=0)
    else:
        return response(receipt)


@bp.route('/add-student', methods=['POST'])
def add_student():
    data = request.json
    token = request.headers.get('token')
    name = data['name']
    receipt = contract.add_student(name,token)
    if (receipt == 1):
        return response(data="error", status_code=0)
    else:
        return response(receipt)


@bp.route('/delete-student', methods=['POST'])
def delete_student():
    data = request.json
    id = data['id']
    token = request.headers.get('token')
    res = db.delete_student(id)
    if res != 0 :
        return response(data="error", status_code=0)
    else:
        receipt = contract.delete_student(id,token)
        if (receipt == 1):
            return response(data="error", status_code=0)
        else:
            return response(receipt)


@bp.route('/update-student', methods=['POST'])
def update_student():
    data = request.json
    id = data['id']
    name = data['name']
    token = request.headers.get('token')
    res = db.update_student(id,name)
    if res != 0 :
        return response(data="error", status_code=0)
    else:
        receipt = contract.update_student(id,name,token)
        if (receipt == 1):
            return response(data="error", status_code=0)
        else:
            return response(receipt)


@bp.route('/add-score', methods=['POST'])
def add_score():
    data = request.json
    token = request.headers.get('token')
    id = data['id']
    subject = data['subject']
    score = data['score']
    receipt = contract.add_student_score(id,subject,score,token)
    if (receipt == 1):
        return response(data="error", status_code=0)
    else:
        return response(receipt)


@bp.route('/update-score', methods=['POST'])
def update_score():
    token = request.headers.get('token')
    data = request.json
    id = data['id']
    num = data['num']
    score = data['score']
    receipt = contract.update_student_score(id,num,score,token)
    if (receipt == 1):
        return response(data="error", status_code=0)
    else:
        return response(receipt)


@bp.route('/get-student', methods=['GET'])
def get_student_info():
    token = request.headers.get('token')
    data = request.json
    id = data['id']
    receipt = contract.get_student_info(id,token)
    if (receipt == 1):
        return response(data="error", status_code=0)
    else:
        return response(receipt)


@bp.route('/get-student-score', methods=['POST'])
def get_student_score():
    token = request.headers.get('token')
    data = request.json
    id = data['id']
    receipt = contract.get_student_score(id,token)
    if (receipt == 1):
        return response(data="error", status_code=0)
    else:
        return response(receipt)


@bp.route('/admin', methods=['GET'])
def get_admin():
    receipt = contract.get_admin()
    if (receipt == 1):
        return response(data="error", status_code=0)
    else:
        return response(receipt)


@bp.route('/get-course', methods=['GET'])
def get_course():
    receipt = db.get_courses()
    if (receipt == 1):
        return response(data="error", status_code=0)
    else:
        return response(receipt)


@bp.route('/get-all-student', methods=['GET'])
def get_all_student():
    receipt = db.get_all_student()
    if (receipt == 1):
        return response(data="error", status_code=0)
    else:
        return response(receipt)


@bp.route('/check-student', methods=['POST'])
def check_student():
    data = request.json
    id = data['id']
    receipt = db.check_student(id)
    if (receipt == 1):
        return response(data="error", status_code=0)
    else:
        return response(receipt)


@bp.route('/get-user', methods=['GET'])
def get_user():
    receipt = db.get_user()
    if (receipt == 1):
        return response(data="error", status_code=0)
    else:
        return response(receipt)