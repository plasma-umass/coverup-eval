# file: pytutils/lazy/lazy_regex.py:92-95
# asked: {"lines": [92, 93, 94, 95], "branches": [[93, 94], [93, 95]]}
# gained: {"lines": [92, 93, 94, 95], "branches": [[93, 94], [93, 95]]}

import pytest
from pytutils.lazy.lazy_regex import InvalidPattern

def test_invalid_pattern_eq_same_class():
    obj1 = InvalidPattern("pattern1")
    obj2 = InvalidPattern("pattern1")
    assert obj1 == obj2

def test_invalid_pattern_eq_different_class():
    obj1 = InvalidPattern("pattern1")
    obj2 = ValueError("pattern1")
    assert obj1 != obj2
