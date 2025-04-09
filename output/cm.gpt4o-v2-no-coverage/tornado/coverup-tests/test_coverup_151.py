# file: tornado/options.py:660-661
# asked: {"lines": [660, 661], "branches": []}
# gained: {"lines": [660, 661], "branches": []}

import pytest
from tornado.options import _Option

@pytest.mark.parametrize("input_value,expected", [
    ("true", True),
    ("false", False),
    ("1", True),
    ("0", False),
    ("t", True),
    ("f", False),
    ("yes", True),
    ("no", True),
])
def test_parse_bool(input_value, expected):
    option = _Option(name="test", type=str)
    assert option._parse_bool(input_value) == expected
