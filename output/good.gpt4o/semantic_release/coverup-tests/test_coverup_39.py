# file semantic_release/helpers.py:16-39
# lines [16, 17, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
# branches ['27->28', '27->29', '29->30', '29->39', '30->31', '30->32', '32->33', '32->34', '34->35', '34->36']

import pytest
from requests import Session
from requests.adapters import HTTPAdapter
from requests.exceptions import RetryError
from urllib3.util.retry import Retry
from semantic_release.helpers import build_requests_session

def test_build_requests_session_raise_for_status():
    session = build_requests_session(raise_for_status=True)
    assert "response" in session.hooks
    assert len(session.hooks["response"]) == 1

def test_build_requests_session_no_raise_for_status():
    session = build_requests_session(raise_for_status=False)
    assert "response" in session.hooks
    assert len(session.hooks["response"]) == 0

def test_build_requests_session_retry_true():
    session = build_requests_session(retry=True)
    adapter = session.get_adapter("http://")
    assert isinstance(adapter, HTTPAdapter)
    assert isinstance(adapter.max_retries, Retry)

def test_build_requests_session_retry_int():
    session = build_requests_session(retry=5)
    adapter = session.get_adapter("http://")
    assert isinstance(adapter, HTTPAdapter)
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5

def test_build_requests_session_retry_instance():
    retry_instance = Retry(total=3)
    session = build_requests_session(retry=retry_instance)
    adapter = session.get_adapter("http://")
    assert isinstance(adapter, HTTPAdapter)
    assert adapter.max_retries == retry_instance

def test_build_requests_session_invalid_retry():
    with pytest.raises(ValueError, match="retry should be a bool, int or Retry instance."):
        build_requests_session(retry="invalid")

@pytest.fixture(autouse=True)
def cleanup(mocker):
    mocker.stopall()
    yield
    mocker.stopall()
