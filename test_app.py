from app import app

def test_home():
    res = app.test_client().get('/')
    assert res.status_code == 200
    assert b'Hello CI/CD' in res.data

def test_hello():
    res = app.test_client().get('/hello/Alice')
    assert b'Hello, Alice!' in res.data

def test_sum():
    res = app.test_client().get('/sum/3/4')
    assert res.data == b'7'