# file: lib/ansible/plugins/filter/core.py:173-180
# asked: {"lines": [173, 175, 176, 177, 178, 180], "branches": [[175, 176], [175, 177], [177, 178], [177, 180]]}
# gained: {"lines": [173, 175, 176, 177, 178, 180], "branches": [[175, 176], [175, 177], [177, 178], [177, 180]]}

import pytest

from ansible.plugins.filter.core import ternary

def test_ternary_true_value():
    assert ternary(True, 'yes', 'no') == 'yes'

def test_ternary_false_value():
    assert ternary(False, 'yes', 'no') == 'no'

def test_ternary_none_value_with_none_val():
    assert ternary(None, 'yes', 'no', 'maybe') == 'maybe'

def test_ternary_none_value_without_none_val():
    assert ternary(None, 'yes', 'no') == 'no'

def test_ternary_non_boolean_true_value():
    assert ternary(1, 'yes', 'no') == 'yes'

def test_ternary_non_boolean_false_value():
    assert ternary(0, 'yes', 'no') == 'no'
