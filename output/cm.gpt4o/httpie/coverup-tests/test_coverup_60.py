# file httpie/sessions.py:153-156
# lines [153, 154, 155, 156]
# branches []

import pytest
from httpie.sessions import Session
from httpie.config import Config

def test_session_auth_setter(tmp_path):
    config_path = tmp_path / 'config.json'
    config_path.write_text('{}')
    session = Session(path=config_path)
    
    # Test setting auth with correct keys
    auth_data = {'type': 'basic', 'raw_auth': 'user:pass'}
    session.auth = auth_data
    assert session['auth'] == auth_data
    
    # Test setting auth with incorrect keys
    with pytest.raises(AssertionError):
        session.auth = {'type': 'basic', 'username': 'user'}
    
    # Clean up
    del session
