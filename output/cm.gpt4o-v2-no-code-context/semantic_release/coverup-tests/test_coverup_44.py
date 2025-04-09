# file: semantic_release/helpers.py:16-39
# asked: {"lines": [], "branches": [[29, 39]]}
# gained: {"lines": [], "branches": [[29, 39]]}

import pytest
from requests import Session
from requests.adapters import HTTPAdapter
from requests.exceptions import RetryError
from requests.packages.urllib3.util.retry import Retry
from semantic_release.helpers import build_requests_session

def test_build_requests_session_no_retry():
    session = build_requests_session(retry=False)
    assert isinstance(session, Session)
    adapter_http = session.adapters.get("http://")
    adapter_https = session.adapters.get("https://")
    assert adapter_http is None or adapter_http.max_retries.total == 0
    assert adapter_https is None or adapter_https.max_retries.total == 0

def test_build_requests_session_retry_as_bool():
    session = build_requests_session(retry=True)
    assert isinstance(session, Session)
    assert isinstance(session.adapters["http://"], HTTPAdapter)
    assert isinstance(session.adapters["https://"], HTTPAdapter)

def test_build_requests_session_retry_as_int():
    session = build_requests_session(retry=5)
    assert isinstance(session, Session)
    adapter = session.adapters["http://"]
    assert isinstance(adapter, HTTPAdapter)
    assert adapter.max_retries.total == 5

def test_build_requests_session_retry_as_retry_instance():
    retry_instance = Retry(total=3)
    session = build_requests_session(retry=retry_instance)
    assert isinstance(session, Session)
    adapter = session.adapters["http://"]
    assert isinstance(adapter, HTTPAdapter)
    assert adapter.max_retries.total == 3

def test_build_requests_session_invalid_retry():
    with pytest.raises(ValueError, match="retry should be a bool, int or Retry instance."):
        build_requests_session(retry="invalid")

def test_build_requests_session_raise_for_status(monkeypatch):
    class MockResponse:
        def raise_for_status(self):
            raise RetryError("Mocked error")

    session = build_requests_session(raise_for_status=True)
    assert isinstance(session, Session)
    assert "response" in session.hooks
    with pytest.raises(RetryError, match="Mocked error"):
        for hook in session.hooks["response"]:
            hook(MockResponse())
