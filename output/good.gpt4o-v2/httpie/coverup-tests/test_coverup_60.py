# file: httpie/sessions.py:100-102
# asked: {"lines": [100, 101, 102], "branches": []}
# gained: {"lines": [100, 101, 102], "branches": []}

import pytest
from httpie.sessions import Session
from httpie.cli.dicts import RequestHeadersDict

def test_session_headers_property():
    session = Session(path='test_session.json')
    session['headers'] = {'Content-Type': 'application/json'}
    
    headers = session.headers
    assert isinstance(headers, RequestHeadersDict)
    assert headers['Content-Type'] == 'application/json'
