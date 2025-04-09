# file: lib/ansible/module_utils/common/validation.py:414-465
# asked: {"lines": [423, 424, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 456, 458, 459, 460, 461, 463, 465], "branches": [[423, 424], [423, 426], [426, 427], [426, 465], [427, 428], [427, 435], [432, 433], [432, 434], [435, 436], [435, 463], [440, 441], [440, 458], [441, 442], [441, 444], [444, 445], [444, 446], [446, 447], [446, 448], [448, 449], [448, 450], [450, 451], [450, 456], [452, 453], [452, 454], [459, 460], [459, 461]]}
# gained: {"lines": [423, 424, 426, 427, 428, 429, 430, 431, 432, 433, 435, 436, 437, 438, 439, 440, 441, 444, 446, 448, 450, 451, 452, 453, 454, 456, 458, 459, 460, 461, 465], "branches": [[423, 424], [423, 426], [426, 427], [426, 465], [427, 428], [427, 435], [432, 433], [435, 436], [440, 441], [440, 458], [441, 444], [444, 446], [446, 448], [448, 450], [450, 451], [450, 456], [452, 453], [452, 454], [459, 460]]}

import pytest
from ansible.module_utils.common.validation import check_type_dict
from ansible.module_utils.six import string_types

def test_check_type_dict_with_dict():
    value = {'key': 'value'}
    result = check_type_dict(value)
    assert result == value

def test_check_type_dict_with_json_string():
    value = '{"key": "value"}'
    result = check_type_dict(value)
    assert result == {'key': 'value'}

def test_check_type_dict_with_invalid_json_string():
    value = '{"key": "value"'
    with pytest.raises(TypeError, match='unable to evaluate string as dictionary'):
        check_type_dict(value)

def test_check_type_dict_with_key_value_string():
    value = 'key1=value1, key2=value2'
    result = check_type_dict(value)
    assert result == {'key1': 'value1', 'key2': 'value2'}

def test_check_type_dict_with_invalid_key_value_string():
    value = 'key1=value1, key2'
    with pytest.raises(ValueError, match='dictionary update sequence element #1 has length 1; 2 is required'):
        check_type_dict(value)

def test_check_type_dict_with_non_string_non_dict():
    value = 12345
    with pytest.raises(TypeError, match="<class 'int'> cannot be converted to a dict"):
        check_type_dict(value)
