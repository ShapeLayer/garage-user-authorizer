import os
from flask import Flask
from .utils import init_db, init_front, init_datafile, apply_demo_preset
from .config import config as local_config

def create_app(test_config=None):
    # init dependencies
    init_front()
    init_datafile()
    init_db()
    apply_demo_preset()

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    for setting_key in local_config:
        app.config[setting_key] = local_config[setting_key]

    # connect routes using blueprint
    from .routes import api
    from .routes import api_person_list
    from .routes import api_receive_media
    from .routes import api_user
    from .routes import api_userstatic
    from .views import front_bridge
    app.register_blueprint(api.bp)
    app.register_blueprint(api_person_list.bp)
    app.register_blueprint(api_receive_media.bp)
    app.register_blueprint(api_user.bp)
    app.register_blueprint(api_userstatic.bp)
    app.register_blueprint(front_bridge.bp)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
