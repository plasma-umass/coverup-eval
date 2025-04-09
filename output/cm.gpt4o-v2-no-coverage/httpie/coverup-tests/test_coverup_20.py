# file: httpie/sessions.py:68-98
# asked: {"lines": [68, 74, 75, 77, 78, 80, 81, 83, 84, 86, 87, 88, 89, 90, 92, 93, 94, 96, 98], "branches": [[75, 77], [75, 98], [77, 78], [77, 80], [80, 81], [80, 83], [83, 84], [83, 86], [86, 87], [86, 92], [87, 88], [87, 89], [92, 93], [92, 96], [93, 92], [93, 94]]}
# gained: {"lines": [68, 74, 75, 77, 78, 80, 81, 83, 84, 86, 87, 88, 89, 90, 92, 93, 94, 96, 98], "branches": [[75, 77], [75, 98], [77, 78], [77, 80], [80, 81], [80, 83], [83, 84], [83, 86], [86, 87], [86, 92], [87, 88], [87, 89], [92, 93], [92, 96], [93, 92], [93, 94]]}

import pytest
from httpie.sessions import Session
from httpie.cli.dicts import RequestHeadersDict
from http.cookies import SimpleCookie

SESSION_IGNORED_HEADER_PREFIXES = ['X-Ignore-']

@pytest.fixture
def session():
    return Session(path='test_session.json')

def test_update_headers_with_none_value(session):
    request_headers = RequestHeadersDict({'Header1': None})
    session.update_headers(request_headers)
    assert 'Header1' not in session.headers

def test_update_headers_with_non_str_value(session):
    request_headers = RequestHeadersDict({'Header2': b'value'})
    session.update_headers(request_headers)
    assert session.headers['Header2'] == 'value'

def test_update_headers_with_user_agent(session):
    request_headers = RequestHeadersDict({'User-Agent': 'HTTPie/1.0.0'})
    session.update_headers(request_headers)
    assert 'User-Agent' not in session.headers

def test_update_headers_with_cookie(session):
    request_headers = RequestHeadersDict({'Cookie': 'cookie1=value1; cookie2=value2'})
    session.update_headers(request_headers)
    assert session['cookies']['cookie1']['value'] == 'value1'
    assert session['cookies']['cookie2']['value'] == 'value2'
    assert 'Cookie' not in request_headers

def test_update_headers_with_ignored_prefix(session, monkeypatch):
    monkeypatch.setattr('httpie.sessions.SESSION_IGNORED_HEADER_PREFIXES', ['X-Ignore-'])
    request_headers = RequestHeadersDict({'X-Ignore-Header': 'value'})
    session.update_headers(request_headers)
    assert 'X-Ignore-Header' not in session.headers

def test_update_headers_with_normal_header(session):
    request_headers = RequestHeadersDict({'Header3': 'value3'})
    session.update_headers(request_headers)
    assert session.headers['Header3'] == 'value3'

@pytest.fixture(autouse=True)
def cleanup(request):
    def remove_test_session():
        import os
        try:
            os.remove('test_session.json')
        except OSError:
            pass
    request.addfinalizer(remove_test_session)
