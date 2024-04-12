# file lib/ansible/utils/_junit_xml.py:261-263
# lines [261, 263]
# branches []

import pytest
from ansible.utils._junit_xml import _attributes

def test_attributes():
    # Test with all values not None
    attrs = _attributes(key1='value1', key2='value2', key3=3)
    assert attrs == {'key1': 'value1', 'key2': 'value2', 'key3': '3'}

    # Test with some values as None
    attrs_with_none = _attributes(key1='value1', key2=None, key3=3)
    assert attrs_with_none == {'key1': 'value1', 'key3': '3'}

    # Test with all values as None
    all_none_attrs = _attributes(key1=None, key2=None, key3=None)
    assert all_none_attrs == {}

    # Test with no arguments
    no_args_attrs = _attributes()
    assert no_args_attrs == {}

    # Test with boolean values
    bool_attrs = _attributes(key1=True, key2=False)
    assert bool_attrs == {'key1': 'True', 'key2': 'False'}

    # Test with mixed types
    mixed_attrs = _attributes(key1=1, key2=2.5, key3=None, key4='string', key5=True)
    assert mixed_attrs == {'key1': '1', 'key2': '2.5', 'key4': 'string', 'key5': 'True'}
