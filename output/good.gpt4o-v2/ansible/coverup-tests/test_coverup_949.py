# file: lib/ansible/modules/systemd.py:295-296
# asked: {"lines": [295, 296], "branches": []}
# gained: {"lines": [295, 296], "branches": []}

import pytest
from ansible.modules.systemd import request_was_ignored

def test_request_was_ignored_no_equal_sign():
    assert request_was_ignored("ignoring request") is True
    assert request_was_ignored("ignoring command") is True
    assert request_was_ignored("some other message") is False

def test_request_was_ignored_with_equal_sign():
    assert request_was_ignored("key=value ignoring request") is False
    assert request_was_ignored("key=value ignoring command") is False
    assert request_was_ignored("key=value some other message") is False
