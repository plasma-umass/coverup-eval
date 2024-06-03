# file lib/ansible/module_utils/common/parameters.py:347-369
# lines []
# branches ['352->354']

import pytest
from ansible.module_utils.common.parameters import _return_datastructure_name

def test_return_datastructure_name_empty_string():
    result = list(_return_datastructure_name(''))
    assert result == []

def test_return_datastructure_name_non_empty_string():
    result = list(_return_datastructure_name('test'))
    assert result == ['test']

def test_return_datastructure_name_empty_bytes():
    result = list(_return_datastructure_name(b''))
    assert result == []

def test_return_datastructure_name_non_empty_bytes():
    result = list(_return_datastructure_name(b'test'))
    assert result == ['test']

@pytest.fixture
def mock_to_native(mocker):
    return mocker.patch('ansible.module_utils.common.parameters.to_native', side_effect=lambda x, **kwargs: x.decode() if isinstance(x, bytes) else x)

def test_return_datastructure_name_empty_string_with_mock(mock_to_native):
    result = list(_return_datastructure_name(''))
    assert result == []
    mock_to_native.assert_not_called()

def test_return_datastructure_name_non_empty_string_with_mock(mock_to_native):
    result = list(_return_datastructure_name('test'))
    assert result == ['test']
    mock_to_native.assert_called_once_with('test', errors='surrogate_or_strict')

def test_return_datastructure_name_empty_bytes_with_mock(mock_to_native):
    result = list(_return_datastructure_name(b''))
    assert result == []
    mock_to_native.assert_not_called()

def test_return_datastructure_name_non_empty_bytes_with_mock(mock_to_native):
    result = list(_return_datastructure_name(b'test'))
    assert result == ['test']
    mock_to_native.assert_called_once_with(b'test', errors='surrogate_or_strict')
