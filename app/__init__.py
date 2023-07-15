import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required

from app import config
from app.dashboard.callbacks import register_callbacks

db = SQLAlchemy()
login = LoginManager()
login.login_view = '/'

def create_app():

    app = Flask(__name__, instance_relative_config=True)

    if os.environ.get('FLASK_ENV') == 'development':
        app.config.from_object(config.DevelopmentConfig())
    elif os.environ.get('FLASK_ENV') == 'production':
        app.config.from_object(config.ProductionConfig())
    else:
        app.config.from_object(config.Config())
        
    from app.dashboard.dash_app import dashApp
    from app.auth.auth_routes import bp as auth_bp
    
    db.init_app(app)
    login.init_app(app)
    app.register_blueprint(auth_bp)
    
    dash = dashApp(app.config["ROUTES_PATHNAME_PREFIX"])
    dash.title = 'Dashboard'
    
    dash.init_app(app=app)
    
    _protect_dashviews(dash)
    
    register_callbacks(dash)
    
    return app
    
def _protect_dashviews(dashapp):
    for view_func in dashapp.server.view_functions:
        if view_func.startswith(dashapp.config.routes_pathname_prefix):
            dashapp.server.view_functions[view_func] = login_required(dashapp.server.view_functions[view_func])
