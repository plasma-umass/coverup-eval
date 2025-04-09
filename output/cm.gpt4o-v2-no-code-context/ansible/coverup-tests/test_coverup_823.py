# file: lib/ansible/modules/systemd.py:295-296
# asked: {"lines": [295, 296], "branches": []}
# gained: {"lines": [295, 296], "branches": []}

import pytest

from ansible.modules.systemd import request_was_ignored

def test_request_was_ignored_with_ignored_request():
    out = "ignoring request"
    assert request_was_ignored(out) == True

def test_request_was_ignored_with_ignored_command():
    out = "ignoring command"
    assert request_was_ignored(out) == True

def test_request_was_ignored_with_no_ignore():
    out = "some other output"
    assert request_was_ignored(out) == False

def test_request_was_ignored_with_equals_sign():
    out = "key=value"
    assert request_was_ignored(out) == False
