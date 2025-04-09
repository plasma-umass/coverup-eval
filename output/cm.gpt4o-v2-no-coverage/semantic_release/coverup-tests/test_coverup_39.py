# file: semantic_release/helpers.py:16-39
# asked: {"lines": [16, 17, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], "branches": [[27, 28], [27, 29], [29, 30], [29, 39], [30, 31], [30, 32], [32, 33], [32, 34], [34, 35], [34, 36]]}
# gained: {"lines": [16, 17, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], "branches": [[27, 28], [27, 29], [29, 30], [29, 39], [30, 31], [30, 32], [32, 33], [32, 34], [34, 35], [34, 36]]}

import pytest
from requests import Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from semantic_release.helpers import build_requests_session

def test_build_requests_session_default():
    session = build_requests_session()
    assert isinstance(session, Session)
    assert 'response' in session.hooks
    assert callable(session.hooks['response'][0])
    assert isinstance(session.get_adapter('http://'), HTTPAdapter)
    assert isinstance(session.get_adapter('https://'), HTTPAdapter)

def test_build_requests_session_no_raise_for_status():
    session = build_requests_session(raise_for_status=False)
    assert isinstance(session, Session)
    assert 'response' in session.hooks
    assert session.hooks['response'] == []

def test_build_requests_session_retry_false():
    session = build_requests_session(retry=False)
    assert isinstance(session, Session)
    assert 'response' in session.hooks
    assert callable(session.hooks['response'][0])
    assert session.get_adapter('http://').max_retries.total == 0
    assert session.get_adapter('https://').max_retries.total == 0

def test_build_requests_session_retry_int():
    session = build_requests_session(retry=5)
    assert isinstance(session, Session)
    assert 'response' in session.hooks
    assert callable(session.hooks['response'][0])
    assert isinstance(session.get_adapter('http://').max_retries, Retry)
    assert session.get_adapter('http://').max_retries.total == 5
    assert isinstance(session.get_adapter('https://').max_retries, Retry)
    assert session.get_adapter('https://').max_retries.total == 5

def test_build_requests_session_retry_instance():
    retry_instance = Retry(total=3)
    session = build_requests_session(retry=retry_instance)
    assert isinstance(session, Session)
    assert 'response' in session.hooks
    assert callable(session.hooks['response'][0])
    assert session.get_adapter('http://').max_retries == retry_instance
    assert session.get_adapter('https://').max_retries == retry_instance

def test_build_requests_session_invalid_retry():
    with pytest.raises(ValueError, match="retry should be a bool, int or Retry instance."):
        build_requests_session(retry="invalid")
