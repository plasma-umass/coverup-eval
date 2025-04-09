# file: lib/ansible/module_utils/api.py:96-118
# asked: {"lines": [98, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 117, 118], "branches": [[102, 0], [102, 103], [104, 105], [106, 107], [106, 108], [112, 113], [112, 114]]}
# gained: {"lines": [98, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 117, 118], "branches": [[102, 103], [104, 105], [106, 107], [106, 108], [112, 113], [112, 114]]}

import pytest
import time

# Import the retry function from the module
from ansible.module_utils.api import retry

# Mock time.sleep to avoid actual waiting during tests
@pytest.fixture(autouse=True)
def mock_sleep(monkeypatch):
    monkeypatch.setattr(time, 'sleep', lambda x: None)

def test_retry_success():
    @retry(retries=3, retry_pause=1)
    def always_succeed():
        return True

    result = always_succeed()
    assert result is True

def test_retry_failure():
    @retry(retries=3, retry_pause=1)
    def always_fail():
        raise Exception("Failure")

    with pytest.raises(Exception, match="Retry limit exceeded: 3"):
        always_fail()

def test_retry_eventual_success():
    call_count = 0

    @retry(retries=3, retry_pause=1)
    def succeed_after_two_tries():
        nonlocal call_count
        call_count += 1
        if call_count < 2:
            raise Exception("Failure")
        return True

    result = succeed_after_two_tries()
    assert result is True
    assert call_count == 2

def test_retry_no_retries():
    @retry(retries=1, retry_pause=1)
    def always_fail():
        raise Exception("Failure")

    with pytest.raises(Exception, match="Retry limit exceeded: 1"):
        always_fail()
