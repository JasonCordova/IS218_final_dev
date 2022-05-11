from app.auth.forms import login_form, register_form
from faker import Faker

from wtforms import Form as WTForm
from flask_wtf import Form as FlaskForm
from app.auth import login
from flask_login import current_user
from flask_login import FlaskLoginClient
from tests import conftest
from app import create_app, User

def test_user_login(application):

    with application.test_request_context():

        form = login_form()
        form.email.data = "FAKEUSER@gmail.com"
        form.password.data = "testtest"
        form.submit
        assert form.validate

def test_user_register(application):

    with application.test_request_context():

        form = register_form()
        form.email.data = "FAKEUSER@gmail.com"
        form.password.data = "testtest"
        form.confirm.data = "testtest"
        form.submit
        assert form.validate