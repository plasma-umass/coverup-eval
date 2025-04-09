# file sanic/helpers.py:103-110
# lines [103, 110]
# branches []

import pytest
from sanic.helpers import has_message_body

@pytest.mark.parametrize("status_code, expected", [
    (100, False),  # Continue
    (101, False),  # Switching Protocols
    (102, False),  # Processing
    (200, True),   # OK
    (204, False),  # No Content
    (304, False),  # Not Modified
    (400, True),   # Bad Request
    (500, True),   # Internal Server Error
])
def test_has_message_body(status_code, expected):
    assert has_message_body(status_code) == expected
