# file sanic/helpers.py:103-110
# lines [103, 110]
# branches []

import pytest
from sanic.helpers import has_message_body

def test_has_message_body():
    # Test cases where message body should not be included
    assert not has_message_body(100)
    assert not has_message_body(150)
    assert not has_message_body(199)
    assert not has_message_body(204)
    assert not has_message_body(304)

    # Test cases where message body should be included
    assert has_message_body(200)
    assert has_message_body(201)
    assert has_message_body(202)
    assert has_message_body(203)
    assert has_message_body(205)
    assert has_message_body(300)
    assert has_message_body(305)
    assert has_message_body(400)
    assert has_message_body(500)
