# file tornado/options.py:660-661
# lines [660, 661]
# branches []

import pytest
from tornado.options import _Option

class TestOption:
    @pytest.fixture
    def option(self):
        return _Option(name="test_option", default=None, type=str, help=None, metavar=None, multiple=False)

    @pytest.mark.parametrize("input_value, expected", [
        ("true", True),
        ("false", False),
        ("1", True),
        ("0", False),
        ("t", True),
        ("f", False),
        ("yes", True),
        ("no", True),
    ])
    def test_parse_bool(self, option, input_value, expected):
        assert option._parse_bool(input_value) == expected
