# file lib/ansible/modules/systemd.py:295-296
# lines [295, 296]
# branches []

import pytest
from unittest.mock import patch

# Assuming the function request_was_ignored is part of a class or module, we need to import it.
# For this example, let's assume it's a standalone function in a module named systemd.

from ansible.modules.systemd import request_was_ignored

@pytest.mark.parametrize("output, expected", [
    ("ignoring request", True),
    ("ignoring command", True),
    ("some other output", False),
    ("key=value ignoring request", False),
    ("key=value ignoring command", False),
])
def test_request_was_ignored(output, expected):
    assert request_was_ignored(output) == expected
