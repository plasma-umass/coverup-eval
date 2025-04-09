# file: lib/ansible/utils/_junit_xml.py:261-263
# asked: {"lines": [261, 263], "branches": []}
# gained: {"lines": [261, 263], "branches": []}

import pytest

from ansible.utils._junit_xml import _attributes

def test_attributes_all_none():
    result = _attributes(a=None, b=None, c=None)
    assert result == {}

def test_attributes_mixed_values():
    result = _attributes(a=1, b=None, c='test', d=3.14)
    assert result == {'a': '1', 'c': 'test', 'd': '3.14'}

def test_attributes_all_valid():
    result = _attributes(a=1, b=2, c=3)
    assert result == {'a': '1', 'b': '2', 'c': '3'}

def test_attributes_empty():
    result = _attributes()
    assert result == {}
