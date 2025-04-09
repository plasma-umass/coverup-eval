# file lib/ansible/module_utils/common/text/converters.py:305-322
# lines [305, 312, 314, 315, 316, 317, 318, 319, 320, 322]
# branches ['312->314', '312->315', '315->316', '315->317', '317->318', '317->319', '319->320', '319->322']

import pytest
from ansible.module_utils.common.text.converters import container_to_text
from ansible.module_utils._text import to_text
from ansible.module_utils.six import binary_type, iteritems
from unittest.mock import call

@pytest.fixture
def mock_to_text(mocker):
    return mocker.patch('ansible.module_utils.common.text.converters.to_text', return_value='mocked_text')

def test_container_to_text_with_binary_type(mock_to_text):
    binary_input = b'some binary data'
    result = container_to_text(binary_input)
    mock_to_text.assert_called_once_with(binary_input, encoding='utf-8', errors='surrogate_or_strict')
    assert result == 'mocked_text'

def test_container_to_text_with_dict(mock_to_text):
    dict_input = {b'key': b'value'}
    result = container_to_text(dict_input)
    expected_calls = [
        call(b'key', encoding='utf-8', errors='surrogate_or_strict'),
        call(b'value', encoding='utf-8', errors='surrogate_or_strict')
    ]
    assert mock_to_text.call_args_list == expected_calls
    assert result == {'mocked_text': 'mocked_text'}

def test_container_to_text_with_list(mock_to_text):
    list_input = [b'item1', b'item2']
    result = container_to_text(list_input)
    expected_calls = [
        call(b'item1', encoding='utf-8', errors='surrogate_or_strict'),
        call(b'item2', encoding='utf-8', errors='surrogate_or_strict')
    ]
    assert mock_to_text.call_args_list == expected_calls
    assert result == ['mocked_text', 'mocked_text']

def test_container_to_text_with_tuple(mock_to_text):
    tuple_input = (b'item1', b'item2')
    result = container_to_text(tuple_input)
    expected_calls = [
        call(b'item1', encoding='utf-8', errors='surrogate_or_strict'),
        call(b'item2', encoding='utf-8', errors='surrogate_or_strict')
    ]
    assert mock_to_text.call_args_list == expected_calls
    assert result == ('mocked_text', 'mocked_text')

def test_container_to_text_with_other_type(mock_to_text):
    other_input = 'already_text'
    result = container_to_text(other_input)
    mock_to_text.assert_not_called()
    assert result == 'already_text'
