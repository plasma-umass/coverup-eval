# file: lib/ansible/plugins/filter/core.py:76-84
# asked: {"lines": [76, 78, 79, 80, 81, 82, 83, 84], "branches": [[78, 79], [78, 80], [80, 81], [80, 82], [82, 83], [82, 84]]}
# gained: {"lines": [76, 78, 79, 80, 81, 82, 83, 84], "branches": [[78, 79], [78, 80], [80, 81], [80, 82], [82, 83], [82, 84]]}

import pytest
from ansible.plugins.filter.core import to_bool

def test_to_bool_with_none():
    assert to_bool(None) is None

def test_to_bool_with_bool_true():
    assert to_bool(True) is True

def test_to_bool_with_bool_false():
    assert to_bool(False) is False

def test_to_bool_with_string_yes():
    assert to_bool('yes') is True

def test_to_bool_with_string_on():
    assert to_bool('on') is True

def test_to_bool_with_string_1():
    assert to_bool('1') is True

def test_to_bool_with_string_true():
    assert to_bool('true') is True

def test_to_bool_with_string_no():
    assert to_bool('no') is False

def test_to_bool_with_integer_1():
    assert to_bool(1) is True

def test_to_bool_with_integer_0():
    assert to_bool(0) is False

def test_to_bool_with_unexpected_string():
    assert to_bool('unexpected') is False
