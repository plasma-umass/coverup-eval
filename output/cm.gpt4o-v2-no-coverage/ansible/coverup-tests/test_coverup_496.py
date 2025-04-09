# file: lib/ansible/plugins/filter/core.py:173-180
# asked: {"lines": [173, 175, 176, 177, 178, 180], "branches": [[175, 176], [175, 177], [177, 178], [177, 180]]}
# gained: {"lines": [173, 175, 176, 177, 178, 180], "branches": [[175, 176], [175, 177], [177, 178], [177, 180]]}

import pytest
from ansible.plugins.filter.core import ternary

def test_ternary_value_is_none_and_none_val_is_not_none():
    assert ternary(None, 'true', 'false', 'none') == 'none'

def test_ternary_value_is_none_and_none_val_is_none():
    assert ternary(None, 'true', 'false', None) == 'false'

def test_ternary_value_is_true():
    assert ternary(True, 'true', 'false') == 'true'

def test_ternary_value_is_false():
    assert ternary(False, 'true', 'false') == 'false'

def test_ternary_value_is_non_empty_string():
    assert ternary('non-empty', 'true', 'false') == 'true'

def test_ternary_value_is_empty_string():
    assert ternary('', 'true', 'false') == 'false'

def test_ternary_value_is_zero():
    assert ternary(0, 'true', 'false') == 'false'

def test_ternary_value_is_non_zero():
    assert ternary(1, 'true', 'false') == 'true'
