# file: httpie/sessions.py:100-102
# asked: {"lines": [100, 101, 102], "branches": []}
# gained: {"lines": [100, 101, 102], "branches": []}

import pytest
from httpie.sessions import Session
from httpie.cli.dicts import RequestHeadersDict
from pathlib import Path

@pytest.fixture
def session():
    path = Path('/tmp/test_session.json')
    session = Session(path)
    session['headers'] = {'Content-Type': 'application/json'}
    yield session
    if path.exists():
        path.unlink()

def test_session_headers(session):
    headers = session.headers
    assert isinstance(headers, RequestHeadersDict)
    assert headers['Content-Type'] == 'application/json'
