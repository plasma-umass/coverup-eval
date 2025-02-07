# file: lib/ansible/plugins/filter/core.py:76-84
# asked: {"lines": [76, 78, 79, 80, 81, 82, 83, 84], "branches": [[78, 79], [78, 80], [80, 81], [80, 82], [82, 83], [82, 84]]}
# gained: {"lines": [76, 78, 79, 80, 81, 82, 83, 84], "branches": [[78, 79], [78, 80], [80, 81], [80, 82], [82, 83], [82, 84]]}

import pytest
from ansible.plugins.filter.core import to_bool
from ansible.module_utils.six import string_types

def test_to_bool():
    # Test when input is None
    assert to_bool(None) is None

    # Test when input is already a boolean
    assert to_bool(True) is True
    assert to_bool(False) is False

    # Test when input is a string that should be converted to True
    assert to_bool('yes') is True
    assert to_bool('on') is True
    assert to_bool('1') is True
    assert to_bool('true') is True

    # Test when input is a string that should be converted to False
    assert to_bool('no') is False
    assert to_bool('off') is False
    assert to_bool('0') is False
    assert to_bool('false') is False

    # Test when input is an integer that should be converted to True
    assert to_bool(1) is True

    # Test when input is an integer that should be converted to False
    assert to_bool(0) is False

    # Test when input is a string that is not recognized
    assert to_bool('random_string') is False

    # Test when input is a type that is not recognized
    assert to_bool([]) is False
    assert to_bool({}) is False
    assert to_bool(3.14) is False
