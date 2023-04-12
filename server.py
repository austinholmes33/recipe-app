from flask import Flask
from model import db, connect_to_db
from forms import CreateUserForm, LoginForm
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
import jinja2
import crud

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"
app.jinja_env.undefined = jinja2.StrictUndefined

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True)