import mysql.connector

# 连接到 MySQL 数据库
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="student"
)




def get_courses():
    # 创建游标对象
    cursor = connection.cursor()
    query = "SELECT courseName FROM course"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result


def check_student(id):
    # 创建游标对象
    cursor = connection.cursor()
    query = "SELECT name FROM user where type = 2 and id = %s"
    cursor.execute(query, (id,))
    result = cursor.fetchone()
    cursor.close()
    return result



def get_all_student():
    # 创建游标对象
    cursor = connection.cursor()
    query = "SELECT * FROM user where type = 2"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result


def get_user():
    # 创建游标对象
    cursor = connection.cursor()
    query = "SELECT * FROM user where type = 1"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

# 删除学生信息
def delete_student(id):
    # 创建游标对象
    cursor = connection.cursor()
    query = "DELETE FROM user WHERE id = %s"
    cursor.execute(query,(id,))
    try:
        connection.commit()
    except Exception as e:
        print(e)
        cursor.close()
        return 1
    else:
        cursor.close()
        return 0


# 修改学生信息
def update_student(id, name):
    # 创建游标对象
    cursor = connection.cursor()
    query = "UPDATE user SET name = %s WHERE id= %s"
    values = (name, id)
    cursor.execute(query, values)
    try:
        connection.commit()
    except Exception as e:
        print(e)
        cursor.close()
        return 1
    else:
        cursor.close()
        return 0
