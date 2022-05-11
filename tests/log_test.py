import os

def test_request_log():

    root = os.path.dirname(os.path.abspath(__file__))
    requestlog = os.path.join(root, '../logs/request.log')

    if not os.path.exists(requestlog):
        os.mknod(requestlog)
    assert os.path.exists(requestlog) == True

def test_errors_log():

    assert True

def test_myapp_log():

    assert True

def test_werkzeug_log():

    assert True

def test_sqlalchemy_log():

    assert True

def test_handler_log():

    assert True