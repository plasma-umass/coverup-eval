# file sanic/cookies.py:108-120
# lines [110, 114, 117, 118]
# branches ['109->110', '111->exit', '113->114', '116->117']

import pytest
from datetime import datetime
from sanic.cookies import Cookie

@pytest.fixture
def cookie():
    c = Cookie('test', 'test_value')
    c._keys = ['max-age', 'expires']
    yield c

def test_cookie_setitem_unknown_key(cookie):
    with pytest.raises(KeyError):
        cookie['unknown'] = 'value'

def test_cookie_setitem_max_age_not_integer(cookie):
    with pytest.raises(ValueError):
        cookie['max-age'] = 'not-an-integer'

def test_cookie_setitem_expires_not_datetime(cookie):
    with pytest.raises(TypeError):
        cookie['expires'] = 'not-a-datetime'

def test_cookie_setitem_expires_datetime(cookie):
    cookie['expires'] = datetime.now()
    assert isinstance(cookie['expires'], datetime)

def test_cookie_setitem_max_age_integer(cookie):
    cookie['max-age'] = 3600
    assert cookie['max-age'] == 3600

def test_cookie_setitem_false_value(cookie):
    cookie['max-age'] = False
    assert 'max-age' not in cookie
