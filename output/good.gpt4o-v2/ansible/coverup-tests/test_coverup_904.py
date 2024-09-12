# file: lib/ansible/utils/_junit_xml.py:261-263
# asked: {"lines": [261, 263], "branches": []}
# gained: {"lines": [261, 263], "branches": []}

import pytest
from ansible.utils._junit_xml import _attributes

def test_attributes_with_values():
    result = _attributes(a=1, b=2, c=3)
    assert result == {'a': '1', 'b': '2', 'c': '3'}

def test_attributes_with_none_values():
    result = _attributes(a=1, b=None, c=3)
    assert result == {'a': '1', 'c': '3'}

def test_attributes_with_all_none_values():
    result = _attributes(a=None, b=None)
    assert result == {}

def test_attributes_with_no_values():
    result = _attributes()
    assert result == {}
