import os
from app import db,auth
from app.db.models import User, Record
from app.auth.forms import csv_upload
from flask_login import FlaskLoginClient

def test_upload_record(application):

    application.test_client_class = FlaskLoginClient
    user = User('keith@webizly.com', 'testtest')
    db.session.add(user)
    db.session.commit()

    assert user.email == 'keith@webizly.com'
    assert db.session.query(User).count() == 1

    root = os.path.dirname(os.path.abspath(__file__))
    record = os.path.join(root, '../uploads/transactions.csv')

    with application.test_client(user=user) as client:

        response = client.get('/records/upload')
        assert response.status_code == 200

        form = csv_upload()
        form.file = record
        assert form.validate

def test_upload_record_failed(client):

    response = client.get('/records/upload')
    assert response.status_code == 302 # User isn't logged in since we don't have a test_client
    assert db.session.query(User).count() == 0