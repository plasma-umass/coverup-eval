# file lib/ansible/module_utils/common/text/converters.py:286-302
# lines [286, 293, 294, 295, 296, 297, 298, 299, 300, 302]
# branches ['293->294', '293->295', '295->296', '295->297', '297->298', '297->299', '299->300', '299->302']

import pytest
from ansible.module_utils.common.text.converters import container_to_bytes
from ansible.module_utils._text import to_bytes
from ansible.module_utils.six import text_type, iteritems

@pytest.fixture
def mock_to_bytes(mocker):
    mock = mocker.patch('ansible.module_utils.common.text.converters.to_bytes')
    mock.side_effect = lambda x, encoding='utf-8', errors='surrogate_or_strict': x.encode(encoding, errors)
    return mock

def test_container_to_bytes_with_text_type(mock_to_bytes):
    assert container_to_bytes(u'test_string') == b'test_string'
    mock_to_bytes.assert_called_once_with(u'test_string', encoding='utf-8', errors='surrogate_or_strict')

def test_container_to_bytes_with_dict(mock_to_bytes):
    input_dict = {'key1': u'value1', 'key2': u'value2'}
    expected_dict = {b'key1': b'value1', b'key2': b'value2'}
    result = container_to_bytes(input_dict)
    assert result == expected_dict
    # Since the keys and values are converted, there should be 4 calls in total
    assert mock_to_bytes.call_count == 4
    # Check that the keys and values are correctly converted
    for key, value in result.items():
        assert isinstance(key, bytes)
        assert isinstance(value, bytes)

def test_container_to_bytes_with_list(mock_to_bytes):
    input_list = [u'item1', u'item2']
    expected_list = [b'item1', b'item2']
    assert container_to_bytes(input_list) == expected_list
    assert mock_to_bytes.call_count == 2

def test_container_to_bytes_with_tuple(mock_to_bytes):
    input_tuple = (u'item1', u'item2')
    expected_tuple = (b'item1', b'item2')
    assert container_to_bytes(input_tuple) == expected_tuple
    assert mock_to_bytes.call_count == 2

def test_container_to_bytes_with_non_container():
    non_container = 42
    assert container_to_bytes(non_container) == 42
