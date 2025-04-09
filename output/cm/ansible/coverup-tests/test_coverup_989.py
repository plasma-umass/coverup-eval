# file lib/ansible/modules/systemd.py:295-296
# lines [295, 296]
# branches []

import pytest
from ansible.modules.systemd import request_was_ignored

def test_request_was_ignored():
    # Test cases where the request should be considered ignored
    assert request_was_ignored("ignoring request") is True
    assert request_was_ignored("ignoring command") is True
    assert request_was_ignored("some other output without equal sign") is False

    # Test cases where the request should not be considered ignored
    assert request_was_ignored("key=value") is False
    assert request_was_ignored("key=value ignoring request") is False
    assert request_was_ignored("key=value ignoring command") is False

    # Test cases with '=' in the output
    assert request_was_ignored("= ignoring request") is False
    assert request_was_ignored("= ignoring command") is False

    # Test empty string
    assert request_was_ignored("") is False

# Note: No cleanup is necessary for this test as it does not modify any state or external resources.
