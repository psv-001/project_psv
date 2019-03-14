from flask import Flask
from flask_compress import Compress
from flask_script import Manager


def create_app(app_name, config_filename):
    app = Flask(app_name)
    app.config.from_object(config_filename)

    return app

app_name = 'project_psv'
appp = create_app(app_name, "config")
Compress(appp)
MANAGER = Manager(appp)
from app import api_bp
appp.register_blueprint(api_bp, url_prefix='/api')

from Model import db
db.init_app(appp)


if __name__ == "__main__":
    #app = create_app("config")
    #app.run(debug=True)
    MANAGER.run()
