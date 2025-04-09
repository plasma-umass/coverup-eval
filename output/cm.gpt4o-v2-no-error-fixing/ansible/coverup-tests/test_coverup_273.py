# file: lib/ansible/plugins/filter/core.py:173-180
# asked: {"lines": [173, 175, 176, 177, 178, 180], "branches": [[175, 176], [175, 177], [177, 178], [177, 180]]}
# gained: {"lines": [173, 175, 176, 177, 178, 180], "branches": [[175, 176], [175, 177], [177, 178], [177, 180]]}

import pytest
from ansible.plugins.filter.core import ternary

def test_ternary_value_none_with_none_val():
    assert ternary(None, 'true', 'false', 'none') == 'none'

def test_ternary_value_none_without_none_val():
    assert ternary(None, 'true', 'false') == 'false'

def test_ternary_value_true():
    assert ternary(True, 'true', 'false') == 'true'

def test_ternary_value_false():
    assert ternary(False, 'true', 'false') == 'false'

def test_ternary_value_non_bool_true():
    assert ternary(1, 'true', 'false') == 'true'

def test_ternary_value_non_bool_false():
    assert ternary(0, 'true', 'false') == 'false'
