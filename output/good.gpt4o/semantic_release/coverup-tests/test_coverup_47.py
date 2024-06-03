# file semantic_release/helpers.py:16-39
# lines []
# branches ['29->39']

import pytest
from requests import Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from semantic_release.helpers import build_requests_session

def test_build_requests_session_without_retry():
    session = build_requests_session(retry=False)
    assert isinstance(session, Session)
    # Ensure that the adapter is the default one without retries
    default_adapter = HTTPAdapter()
    assert type(session.get_adapter("http://")) == type(default_adapter)
    assert type(session.get_adapter("https://")) == type(default_adapter)

def test_build_requests_session_with_retry_bool():
    session = build_requests_session(retry=True)
    assert isinstance(session, Session)
    assert isinstance(session.get_adapter("http://"), HTTPAdapter)
    assert isinstance(session.get_adapter("https://"), HTTPAdapter)

def test_build_requests_session_with_retry_int():
    session = build_requests_session(retry=5)
    assert isinstance(session, Session)
    assert isinstance(session.get_adapter("http://"), HTTPAdapter)
    assert isinstance(session.get_adapter("https://"), HTTPAdapter)

def test_build_requests_session_with_retry_instance():
    retry_instance = Retry(total=3)
    session = build_requests_session(retry=retry_instance)
    assert isinstance(session, Session)
    assert isinstance(session.get_adapter("http://"), HTTPAdapter)
    assert isinstance(session.get_adapter("https://"), HTTPAdapter)

def test_build_requests_session_with_invalid_retry():
    with pytest.raises(ValueError, match="retry should be a bool, int or Retry instance."):
        build_requests_session(retry="invalid")

@pytest.fixture(autouse=True)
def cleanup(mocker):
    # Clean up any global state or side effects here
    yield
    # Add any necessary cleanup code here
