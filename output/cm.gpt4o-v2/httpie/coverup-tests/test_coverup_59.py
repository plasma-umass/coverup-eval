# file: httpie/sessions.py:153-156
# asked: {"lines": [153, 154, 155, 156], "branches": []}
# gained: {"lines": [153, 154, 155, 156], "branches": []}

import pytest
from httpie.sessions import Session

def test_session_auth_setter():
    session = Session(path='test_session.json')
    
    valid_auth = {'type': 'basic', 'raw_auth': 'user:pass'}
    session.auth = valid_auth
    assert session['auth'] == valid_auth

    with pytest.raises(AssertionError):
        session.auth = {'type': 'basic'}

    with pytest.raises(AssertionError):
        session.auth = {'raw_auth': 'user:pass'}

    with pytest.raises(AssertionError):
        session.auth = {'type': 'basic', 'raw_auth': 'user:pass', 'extra_key': 'value'}
