# file: lib/ansible/modules/systemd.py:295-296
# asked: {"lines": [295, 296], "branches": []}
# gained: {"lines": [295, 296], "branches": []}

import pytest

from ansible.modules.systemd import request_was_ignored

@pytest.mark.parametrize("output, expected", [
    ("ignoring request", True),
    ("ignoring command", True),
    ("some random output", False),
    ("key=value ignoring request", False),
    ("key=value ignoring command", False),
    ("", False),
])
def test_request_was_ignored(output, expected):
    assert request_was_ignored(output) == expected
