from app import db
from app.db.models import User

from flask_login import FlaskLoginClient
from app.auth.forms import *

def test_dashboard_accessed(application):

    application.test_client_class = FlaskLoginClient # Sets a fake testing client

    user = User('keith@webizly.com', 'testtest')
    db.session.add(user)
    db.session.commit() # What we did so far was just make keith@webizly a fake user as done from auth_test

    assert user.email == 'keith@webizly.com'
    assert db.session.query(User).count() == 1 # Make sure keith@webizly.com is the only user.

    with application.test_client(user=user) as client:

        response = client.get('/dashboard')
        assert b'keith@webizly.com' in response.data
        assert response.status_code == 200 # Successful access to dashboard as user keith@webizly.com

def test_dashboard_declined(application):

    application.test_client_class = FlaskLoginClient
    assert db.session.query(User).count() == 0

    with application.test_client(user = None) as client: # Have the client NOT be signed in.

        response = client.get('/dashboard')
        assert response.status_code == 302 # 302 is the access denied status code.