import mysql.connector

# 连接到 MySQL 数据库
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="student"
)

# 创建游标对象
cursor = connection.cursor()
