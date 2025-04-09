# file: lib/ansible/modules/systemd.py:295-296
# asked: {"lines": [295, 296], "branches": []}
# gained: {"lines": [295, 296], "branches": []}

import pytest
from ansible.modules.systemd import request_was_ignored

def test_request_was_ignored():
    assert request_was_ignored("ignoring request") == True
    assert request_was_ignored("ignoring command") == True
    assert request_was_ignored("some other output") == False
    assert request_was_ignored("key=value ignoring request") == False
    assert request_was_ignored("key=value ignoring command") == False
