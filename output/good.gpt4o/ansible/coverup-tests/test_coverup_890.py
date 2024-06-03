# file lib/ansible/utils/_junit_xml.py:261-263
# lines [261, 263]
# branches []

import pytest
from ansible.utils._junit_xml import _attributes

def test_attributes():
    # Test with various types of values
    result = _attributes(a=1, b=None, c="test", d=4.5, e=False)
    assert result == {"a": "1", "c": "test", "d": "4.5", "e": "False"}

    # Test with all None values
    result = _attributes(a=None, b=None)
    assert result == {}

    # Test with no arguments
    result = _attributes()
    assert result == {}

    # Test with special characters
    result = _attributes(a="!@#$%^&*()")
    assert result == {"a": "!@#$%^&*()"}

    # Test with boolean values
    result = _attributes(a=True, b=False)
    assert result == {"a": "True", "b": "False"}
