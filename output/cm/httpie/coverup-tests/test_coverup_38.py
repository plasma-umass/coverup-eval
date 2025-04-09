# file httpie/sessions.py:153-156
# lines [153, 154, 155, 156]
# branches []

import pytest
from httpie.sessions import Session

def test_session_auth_setter(tmp_path):
    session = Session(str(tmp_path / 'session.json'))
    auth_dict = {'type': 'basic', 'raw_auth': 'user:pass'}

    # Set the auth property
    session.auth = auth_dict

    # Verify that the auth property was set correctly
    assert session['auth'] == auth_dict

    # Clean up the session file after the test
    session_path = tmp_path / 'session.json'
    if session_path.exists():
        session_path.unlink()

def test_session_auth_setter_invalid_keys(tmp_path):
    session = Session(str(tmp_path / 'session.json'))
    invalid_auth_dict = {'wrong_key': 'value'}

    # Verify that setting the auth property with invalid keys raises an AssertionError
    with pytest.raises(AssertionError):
        session.auth = invalid_auth_dict

    # Clean up the session file after the test
    session_path = tmp_path / 'session.json'
    if session_path.exists():
        session_path.unlink()
