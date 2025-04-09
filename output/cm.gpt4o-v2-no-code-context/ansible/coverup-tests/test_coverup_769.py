# file: lib/ansible/utils/_junit_xml.py:261-263
# asked: {"lines": [261, 263], "branches": []}
# gained: {"lines": [261, 263], "branches": []}

import pytest
from ansible.utils._junit_xml import _attributes

def test_attributes_with_none_values():
    result = _attributes(a=1, b=None, c='test', d=None)
    assert result == {'a': '1', 'c': 'test'}

def test_attributes_all_none_values():
    result = _attributes(a=None, b=None)
    assert result == {}

def test_attributes_no_none_values():
    result = _attributes(a=1, b=2, c='test')
    assert result == {'a': '1', 'b': '2', 'c': 'test'}
