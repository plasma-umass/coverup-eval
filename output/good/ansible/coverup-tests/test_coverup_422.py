# file lib/ansible/plugins/filter/core.py:173-180
# lines [173, 175, 176, 177, 178, 180]
# branches ['175->176', '175->177', '177->178', '177->180']

import pytest
from ansible.plugins.filter.core import ternary

def test_ternary():
    assert ternary(True, 'yes', 'no') == 'yes', "True should return true_val"
    assert ternary(False, 'yes', 'no') == 'no', "False should return false_val"
    assert ternary(None, 'yes', 'no', 'maybe') == 'maybe', "None with none_val should return none_val"
    assert ternary(None, 'yes', 'no') == 'no', "None without none_val should return false_val"

# Ensure the test does not affect other tests by not having any side effects
