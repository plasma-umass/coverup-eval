# file lib/ansible/module_utils/common/validation.py:414-465
# lines [423, 424, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 456, 458, 459, 460, 461, 463, 465]
# branches ['423->424', '423->426', '426->427', '426->465', '427->428', '427->435', '432->433', '432->434', '435->436', '435->463', '440->441', '440->458', '441->442', '441->444', '444->445', '444->446', '446->447', '446->448', '448->449', '448->450', '450->451', '450->456', '452->453', '452->454', '459->460', '459->461']

import pytest
from ansible.module_utils.common.validation import check_type_dict

def test_check_type_dict_with_dict():
    assert check_type_dict({'key': 'value'}) == {'key': 'value'}

def test_check_type_dict_with_json_string():
    assert check_type_dict('{"key": "value"}') == {'key': 'value'}

def test_check_type_dict_with_invalid_json_string():
    with pytest.raises(TypeError, match="unable to evaluate string as dictionary"):
        check_type_dict('{key: value}')

def test_check_type_dict_with_key_value_string():
    assert check_type_dict('key1=value1, key2=value2') == {'key1': 'value1', 'key2': 'value2'}

def test_check_type_dict_with_escaped_characters():
    assert check_type_dict('key1=value1\\,value2, key2=value3') == {'key1': 'value1,value2', 'key2': 'value3'}

def test_check_type_dict_with_quotes():
    assert check_type_dict('key1="value1, value2", key2=\'value3\'') == {'key1': 'value1, value2', 'key2': 'value3'}

def test_check_type_dict_with_invalid_string():
    with pytest.raises(TypeError, match="dictionary requested, could not parse JSON or key=value"):
        check_type_dict('not a valid dictionary')

def test_check_type_dict_with_unsupported_type():
    with pytest.raises(TypeError, match="cannot be converted to a dict"):
        check_type_dict([1, 2, 3])
