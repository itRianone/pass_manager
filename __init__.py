# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///password_manager.sqlite3 '
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
# migrate.init_app(app, db)
#from script import app, db, migrate
#with app.app_context():
#    if db.engine.url.drivername == 'sqlite':
#        migrate.init_app(app, db, render_as_batch=True)
#    else:
#        migrate.init_app(app, db)