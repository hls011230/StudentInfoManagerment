# app.py

from flask import Flask
from controller.controller import bp as api_bp

def create_app():
    app = Flask(__name__,static_folder="static")

    # 注册蓝图
    app.register_blueprint(api_bp)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)


