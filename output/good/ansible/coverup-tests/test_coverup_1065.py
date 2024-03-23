# file lib/ansible/module_utils/splitter.py:211-212
# lines [211, 212]
# branches []

import pytest
from ansible.module_utils.splitter import is_quoted

def test_is_quoted():
    assert is_quoted('') == False, "Empty string should not be considered quoted"
    assert is_quoted('"double quoted"') == True, "Double quoted string should be considered quoted"
    assert is_quoted("'single quoted'") == True, "Single quoted string should be considered quoted"
    assert is_quoted('no quotes') == False, "String without quotes should not be considered quoted"
    assert is_quoted('"mismatched\'') == False, "Mismatched quotes should not be considered quoted"
    assert is_quoted('\'mismatched"') == False, "Mismatched quotes should not be considered quoted"
    assert is_quoted('"') == True, "Single double-quote should be considered quoted"
    assert is_quoted("'") == True, "Single single-quote should be considered quoted"
    assert is_quoted('""') == True, "Empty double quoted string should be considered quoted"
    assert is_quoted("''") == True, "Empty single quoted string should be considered quoted"
