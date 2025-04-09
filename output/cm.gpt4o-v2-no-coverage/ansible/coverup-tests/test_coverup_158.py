# file: lib/ansible/plugins/filter/core.py:308-338
# asked: {"lines": [308, 309, 310, 311, 312, 315, 318, 320, 321, 323, 324, 333, 334, 335, 336, 338], "branches": [[311, 312], [311, 315], [320, 321], [320, 323], [323, 324], [323, 333], [335, 336], [335, 338]]}
# gained: {"lines": [308, 309, 310, 311, 312, 315, 318, 320, 321, 323, 324, 333, 334, 335, 336, 338], "branches": [[311, 312], [311, 315], [320, 321], [320, 323], [323, 324], [323, 333], [335, 336], [335, 338]]}

import pytest
from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.core import combine
from ansible.template import recursive_check_defined
from ansible.utils.vars import merge_hash
from unittest.mock import patch

@pytest.fixture
def mock_recursive_check_defined():
    with patch('ansible.plugins.filter.core.recursive_check_defined') as mock:
        yield mock

@pytest.fixture
def mock_merge_hash():
    with patch('ansible.plugins.filter.core.merge_hash') as mock:
        yield mock

@pytest.fixture
def mock_flatten():
    with patch('ansible.plugins.filter.core.flatten') as mock:
        yield mock

def test_combine_no_terms(mock_flatten, mock_recursive_check_defined):
    mock_flatten.return_value = []
    result = combine()
    assert result == {}
    mock_flatten.assert_called_once_with((), levels=1)
    mock_recursive_check_defined.assert_called_once_with([])

def test_combine_single_term(mock_flatten, mock_recursive_check_defined):
    mock_flatten.return_value = [{'key': 'value'}]
    result = combine({'key': 'value'})
    assert result == {'key': 'value'}
    mock_flatten.assert_called_once_with(({'key': 'value'},), levels=1)
    mock_recursive_check_defined.assert_called_once_with([{'key': 'value'}])

def test_combine_multiple_terms(mock_flatten, mock_recursive_check_defined, mock_merge_hash):
    mock_flatten.return_value = [{'key1': 'value1'}, {'key2': 'value2'}]
    mock_merge_hash.side_effect = lambda x, y, recursive, list_merge: {**x, **y}
    result = combine({'key1': 'value1'}, {'key2': 'value2'})
    assert result == {'key1': 'value1', 'key2': 'value2'}
    mock_flatten.assert_called_once_with(({'key1': 'value1'}, {'key2': 'value2'}), levels=1)
    mock_recursive_check_defined.assert_called_once_with([{'key1': 'value1'}, {'key2': 'value2'}])
    mock_merge_hash.assert_called_once_with({'key1': 'value1'}, {'key2': 'value2'}, False, 'replace')

def test_combine_invalid_kwargs():
    with pytest.raises(AnsibleFilterError, match="'recursive' and 'list_merge' are the only valid keyword arguments"):
        combine(invalid_arg=True)

def test_combine_recursive_option(mock_flatten, mock_recursive_check_defined, mock_merge_hash):
    mock_flatten.return_value = [{'key1': 'value1'}, {'key2': 'value2'}]
    mock_merge_hash.side_effect = lambda x, y, recursive, list_merge: {**x, **y}
    result = combine({'key1': 'value1'}, {'key2': 'value2'}, recursive=True)
    assert result == {'key1': 'value1', 'key2': 'value2'}
    mock_flatten.assert_called_once_with(({'key1': 'value1'}, {'key2': 'value2'}), levels=1)
    mock_recursive_check_defined.assert_called_once_with([{'key1': 'value1'}, {'key2': 'value2'}])
    mock_merge_hash.assert_called_once_with({'key1': 'value1'}, {'key2': 'value2'}, True, 'replace')

def test_combine_list_merge_option(mock_flatten, mock_recursive_check_defined, mock_merge_hash):
    mock_flatten.return_value = [{'key1': 'value1'}, {'key2': 'value2'}]
    mock_merge_hash.side_effect = lambda x, y, recursive, list_merge: {**x, **y}
    result = combine({'key1': 'value1'}, {'key2': 'value2'}, list_merge='append')
    assert result == {'key1': 'value1', 'key2': 'value2'}
    mock_flatten.assert_called_once_with(({'key1': 'value1'}, {'key2': 'value2'}), levels=1)
    mock_recursive_check_defined.assert_called_once_with([{'key1': 'value1'}, {'key2': 'value2'}])
    mock_merge_hash.assert_called_once_with({'key1': 'value1'}, {'key2': 'value2'}, False, 'append')
