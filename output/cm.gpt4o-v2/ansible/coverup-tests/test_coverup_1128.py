# file: lib/ansible/module_utils/api.py:96-118
# asked: {"lines": [98, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 117, 118], "branches": [[102, 0], [102, 103], [104, 105], [106, 107], [106, 108], [112, 113], [112, 114]]}
# gained: {"lines": [98, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 117, 118], "branches": [[102, 103], [104, 105], [106, 107], [106, 108], [112, 113], [112, 114]]}

import pytest
import time
from ansible.module_utils.api import retry

def test_retry_decorator_success():
    @retry(retries=3, retry_pause=1)
    def always_succeeds():
        return True

    assert always_succeeds() is True

def test_retry_decorator_failure():
    @retry(retries=3, retry_pause=1)
    def always_fails():
        raise Exception("Failure")

    with pytest.raises(Exception, match="Retry limit exceeded: 3"):
        always_fails()

def test_retry_decorator_eventual_success(monkeypatch):
    call_count = [0]  # Use a list to allow modification within the nested function

    @retry(retries=4, retry_pause=1)
    def succeeds_after_two_tries():
        call_count[0] += 1
        if call_count[0] < 3:
            raise Exception("Failure")
        return True

    assert succeeds_after_two_tries() is True
    assert call_count[0] == 3
