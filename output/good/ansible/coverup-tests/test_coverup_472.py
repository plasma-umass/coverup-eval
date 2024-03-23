# file lib/ansible/utils/vars.py:82-94
# lines [82, 87, 88, 91, 92, 93, 94]
# branches ['87->88', '87->91']

import pytest
from ansible.utils.vars import combine_vars
from ansible.constants import DEFAULT_HASH_BEHAVIOUR

# Mocking the merge_hash function and _validate_mutable_mappings function
@pytest.fixture
def mock_merge_hash(mocker):
    return mocker.patch('ansible.utils.vars.merge_hash', return_value='merged_result')

@pytest.fixture
def mock_validate_mutable_mappings(mocker):
    return mocker.patch('ansible.utils.vars._validate_mutable_mappings')

# Test when merge is True
def test_combine_vars_with_merge_true(mock_merge_hash, mock_validate_mutable_mappings):
    a = {'key1': 'value1'}
    b = {'key2': 'value2'}
    result = combine_vars(a, b, merge=True)
    mock_merge_hash.assert_called_once_with(a, b)
    mock_validate_mutable_mappings.assert_not_called()
    assert result == 'merged_result'

# Test when merge is False
def test_combine_vars_with_merge_false(mock_merge_hash, mock_validate_mutable_mappings):
    a = {'key1': 'value1'}
    b = {'key2': 'value2'}
    result = combine_vars(a, b, merge=False)
    mock_merge_hash.assert_not_called()
    mock_validate_mutable_mappings.assert_called_once_with(a, b)
    assert result == {'key1': 'value1', 'key2': 'value2'}

# Test when merge is None and DEFAULT_HASH_BEHAVIOUR is 'merge'
def test_combine_vars_with_default_merge_behavior(mock_merge_hash, mock_validate_mutable_mappings, mocker):
    mocker.patch('ansible.constants.DEFAULT_HASH_BEHAVIOUR', 'merge')
    a = {'key1': 'value1'}
    b = {'key2': 'value2'}
    result = combine_vars(a, b)
    mock_merge_hash.assert_called_once_with(a, b)
    mock_validate_mutable_mappings.assert_not_called()
    assert result == 'merged_result'

# Test when merge is None and DEFAULT_HASH_BEHAVIOUR is 'replace'
def test_combine_vars_with_default_replace_behavior(mock_merge_hash, mock_validate_mutable_mappings, mocker):
    mocker.patch('ansible.constants.DEFAULT_HASH_BEHAVIOUR', 'replace')
    a = {'key1': 'value1'}
    b = {'key2': 'value2'}
    result = combine_vars(a, b)
    mock_merge_hash.assert_not_called()
    mock_validate_mutable_mappings.assert_called_once_with(a, b)
    assert result == {'key1': 'value1', 'key2': 'value2'}
