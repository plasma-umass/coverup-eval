# file: lib/ansible/module_utils/parsing/convert_bool.py:16-29
# asked: {"lines": [16, 17, 18, 20, 21, 22, 24, 25, 26, 27, 29], "branches": [[17, 18], [17, 20], [21, 22], [21, 24], [24, 25], [24, 26], [26, 27], [26, 29]]}
# gained: {"lines": [16, 17, 18, 20, 21, 22, 24, 25, 26, 27, 29], "branches": [[17, 18], [17, 20], [21, 22], [21, 24], [24, 25], [24, 26], [26, 27], [26, 29]]}

import pytest
from ansible.module_utils.parsing.convert_bool import boolean

def test_boolean_with_bool():
    assert boolean(True) is True
    assert boolean(False) is False

def test_boolean_with_text_type():
    assert boolean('yes') is True
    assert boolean('no') is False

def test_boolean_with_binary_type():
    assert boolean(b'yes') is True
    assert boolean(b'no') is False

def test_boolean_with_invalid_strict():
    with pytest.raises(TypeError):
        boolean('invalid', strict=True)

def test_boolean_with_invalid_non_strict():
    assert boolean('invalid', strict=False) is False

def test_boolean_with_numeric_true():
    assert boolean(1) is True
    assert boolean(1.0) is True

def test_boolean_with_numeric_false():
    assert boolean(0) is False
    assert boolean(0.0) is False
