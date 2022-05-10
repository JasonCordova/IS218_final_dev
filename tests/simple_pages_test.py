"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/about"' in response.data
    assert b'href="/welcome"' in response.data
    assert b'href="/login"' in response.data
    assert b'href="/register"' in response.data


def test_request_index(client):
    """This gets the index page"""
    response = client.get("/")
    assert response.status_code == 200

def test_request_about(client):
    """This gets the about page"""
    response = client.get("/about")
    assert response.status_code == 200

def test_request_page1(client):
    """This gets the welcome page"""
    response = client.get("/welcome")
    assert response.status_code == 200

def test_request_page_not_found(client):
    """This gets a page that does not exist"""
    response = client.get("/page5")
    assert response.status_code == 404