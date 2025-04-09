# file: httpie/sessions.py:100-102
# asked: {"lines": [100, 101, 102], "branches": []}
# gained: {"lines": [100, 101, 102], "branches": []}

import pytest
from httpie.sessions import Session
from httpie.cli.dicts import RequestHeadersDict
from pathlib import Path

@pytest.fixture
def session_with_headers():
    path = Path('/tmp/test_session.json')
    session = Session(path)
    session['headers'] = {'Content-Type': 'application/json'}
    return session

def test_session_headers_property(session_with_headers):
    headers = session_with_headers.headers
    assert isinstance(headers, RequestHeadersDict)
    assert headers['Content-Type'] == 'application/json'

def test_session_headers_property_empty():
    path = Path('/tmp/test_session_empty.json')
    session = Session(path)
    session['headers'] = {}
    headers = session.headers
    assert isinstance(headers, RequestHeadersDict)
    assert len(headers) == 0
