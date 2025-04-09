# file lib/ansible/plugins/filter/core.py:76-84
# lines [76, 78, 79, 80, 81, 82, 83, 84]
# branches ['78->79', '78->80', '80->81', '80->82', '82->83', '82->84']

import pytest
from ansible.plugins.filter.core import to_bool

@pytest.mark.parametrize("input_value,expected", [
    (None, None),
    (True, True),
    (False, False),
    ("YES", True),
    ("on", True),
    ("1", True),
    ("true", True),
    (1, True),
    ("NO", False),
    ("off", False),
    ("0", False),
    ("false", False),
    (0, False),
    ("unexpected_string", False),
    (2, False),
    ([], False),
    ({}, False),
])
def test_to_bool(input_value, expected):
    assert to_bool(input_value) == expected
