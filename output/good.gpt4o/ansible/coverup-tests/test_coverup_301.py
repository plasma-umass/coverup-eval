# file lib/ansible/plugins/filter/core.py:76-84
# lines [76, 78, 79, 80, 81, 82, 83, 84]
# branches ['78->79', '78->80', '80->81', '80->82', '82->83', '82->84']

import pytest
from ansible.plugins.filter.core import to_bool

def test_to_bool():
    # Test with None
    assert to_bool(None) is None

    # Test with boolean values
    assert to_bool(True) is True
    assert to_bool(False) is False

    # Test with string values
    assert to_bool('yes') is True
    assert to_bool('on') is True
    assert to_bool('1') is True
    assert to_bool('true') is True
    assert to_bool('no') is False
    assert to_bool('off') is False
    assert to_bool('0') is False
    assert to_bool('false') is False

    # Test with integer values
    assert to_bool(1) is True
    assert to_bool(0) is False

    # Test with other types
    assert to_bool([]) is False
    assert to_bool({}) is False
    assert to_bool(2) is False
    assert to_bool('random_string') is False
