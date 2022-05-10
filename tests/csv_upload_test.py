import os, logging, io
from werkzeug.datastructures import FileStorage

def test_csv_upload(test_client):

    log = logging.getLogger('myApp')

    root = os.path.dirname(os.path.abspath(__file__))
    dbdir = os.path.join(root, 'fake.csv')

    file = dbdir
    fp = (open(file, 'rb'), file)
    file = FileStorage(fp)
    file.filename = 'test.csv'

    data = {

        #'file': (open(file, 'rb'), file),
        'file': file,
        'submit': True,
        'csrf_token': 'ImY0YzE1MDE2MGE5MDRlMzMwM2E1MTUyNGUwOTdhOTg0OTVkNzJiN2Yi.YnREvQ.duakqz1dioLIFSLlg0i_k1GJnLM'
    }

    log.info(data)

    response = test_client.post("/records/upload", data=data)
    assert response.status_code == 200