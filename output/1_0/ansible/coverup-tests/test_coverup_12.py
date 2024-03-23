# file lib/ansible/module_utils/parsing/convert_bool.py:16-29
# lines [16, 17, 18, 20, 21, 22, 24, 25, 26, 27, 29]
# branches ['17->18', '17->20', '21->22', '21->24', '24->25', '24->26', '26->27', '26->29']

import pytest
from ansible.module_utils.parsing.convert_bool import boolean
from ansible.module_utils._text import to_text, text_type, binary_type

BOOLEANS_TRUE = frozenset(('yes', 'on', '1', 'true', 't', 'y', 'enable', 'enabled'))
BOOLEANS_FALSE = frozenset(('no', 'off', '0', 'false', 'f', 'n', 'disable', 'disabled'))

def test_boolean_strict_invalid_value():
    with pytest.raises(TypeError):
        boolean('invalid_value')

def test_boolean_non_strict_invalid_value():
    assert boolean('invalid_value', strict=False) is False

def test_boolean_with_text_type():
    assert boolean(text_type('yes')) is True

def test_boolean_with_binary_type():
    assert boolean(binary_type(b'no')) is False
