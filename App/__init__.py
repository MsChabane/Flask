from flask  import Flask ,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
 
 
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
app.config['SECRET_KEY']='fc9c841ef67e5f99cc3c1acd43dbe77fbef507006bcd38988622fc75fd997cb5'
db = SQLAlchemy(app)
bcrypt= Bcrypt()
login_manager =  LoginManager(app)
login_manager.login_message_category="info"
login_manager.login_view='login'
with app.app_context():
  db.create_all()


from App import routes