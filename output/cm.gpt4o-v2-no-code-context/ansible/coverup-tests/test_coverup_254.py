# file: lib/ansible/plugins/filter/core.py:76-84
# asked: {"lines": [76, 78, 79, 80, 81, 82, 83, 84], "branches": [[78, 79], [78, 80], [80, 81], [80, 82], [82, 83], [82, 84]]}
# gained: {"lines": [76, 78, 79, 80, 81, 82, 83, 84], "branches": [[78, 79], [78, 80], [80, 81], [80, 82], [82, 83], [82, 84]]}

import pytest
from ansible.plugins.filter.core import to_bool

def test_to_bool_none():
    assert to_bool(None) is None

def test_to_bool_true():
    assert to_bool(True) is True

def test_to_bool_false():
    assert to_bool(False) is False

def test_to_bool_string_true():
    assert to_bool('yes') is True
    assert to_bool('on') is True
    assert to_bool('1') is True
    assert to_bool('true') is True

def test_to_bool_string_false():
    assert to_bool('no') is False
    assert to_bool('off') is False
    assert to_bool('0') is False
    assert to_bool('false') is False

def test_to_bool_int_true():
    assert to_bool(1) is True

def test_to_bool_int_false():
    assert to_bool(0) is False

def test_to_bool_other():
    assert to_bool('random_string') is False
    assert to_bool(2) is False
