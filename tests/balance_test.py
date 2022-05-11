from app import db
from app.db.models import User

from flask_login import FlaskLoginClient
from app.auth.forms import *

def test_balance_calculate(application):

    application.test_client_class = FlaskLoginClient
    user = User('keith@webizly.com', 'testtest')
    db.session.add(user)
    db.session.commit()

    assert user.email == 'keith@webizly.com'
    assert user.balance == 0.00 # Default balance

    user.balance += 5.67
    assert user.balance == 5.67

    user.balance -= 1.00
    assert user.balance == 4.67