import logging

from app import db
from app.db.models import User, Record
from faker import Faker
from werkzeug.security import generate_password_hash
from flask_login import login_user


def test_adding_user(application, client):
    log = logging.getLogger("myApp")
    with application.app_context():
        assert db.session.query(User).count() == 0
        assert db.session.query(Record).count() == 0
        # showing how to add a record
        # create a record
        user = User('keith@webizly.com', generate_password_hash('testtest'))
        # add it to get ready to be committed
        db.session.add(user)
        # call the commit
        # db.session.commit()
        # assert that we now have a new user
        # assert db.session.query(User).count() == 1
        # finding one user record by email
        user = User.query.filter_by(email='keith@webizly.com').first()
        log.info(user)
        # asserting that the user retrieved is correct
        assert user.email == 'keith@webizly.com'

        user.records = [Record(2000, 'CREDIT')]
        # commit is what saves the songs
        db.session.commit()
        # assert db.session.query(Song).count() == 2
        rec1 = Record.query.filter_by(amount=2000).first()
        assert rec1.amount == 2000
        db.session.delete(user)
        db.session.delete(rec1)
        db.session.commit()
        assert db.session.query(User).count() == 0
        assert db.session.query(Record).count() == 0