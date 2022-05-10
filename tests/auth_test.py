"""This test the homepage"""
from app import db
from app.db.models import User
import logging
from flask_login import current_user

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/login"' in response.data
    assert b'href="/register"' in response.data

def test_auth_pages(client):
    """This makes the index page"""
    response = client.get("/dashboard")
    assert response.status_code == 302 # test for denied access to dashboard
    response = client.get("/register")
    assert response.status_code == 200 # test for registration
    response = client.get("/login")
    assert response.status_code == 200 # test for login

def test_upload_access(client):

    response = client.get("/records/upload")
    if (current_user):
        assert response.status_code == 200
    else:
        assert response.status_code == 302# test for denied access to upload song

def test_dashboard_access(client):

    response = client.get("/dashboard")
    if (current_user):
        assert response.status_code == 200
    else:
        assert response.status_code == 302 # test for dashboard access w/ and w/o login