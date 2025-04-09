# file lib/ansible/module_utils/common/collections.py:86-97
# lines [86, 94, 95, 97]
# branches ['94->95', '94->97']

import pytest
from collections.abc import Sequence
from ansible.module_utils.common.collections import is_sequence

# Mocking the is_string function to control its behavior
@pytest.fixture
def mock_is_string(mocker):
    return mocker.patch('ansible.module_utils.common.collections.is_string')

# Test to cover the case when include_strings is False and the input is a string
def test_is_sequence_exclude_strings(mock_is_string):
    mock_is_string.return_value = True
    assert not is_sequence('string', include_strings=False)
    mock_is_string.assert_called_once_with('string')

# Test to cover the case when include_strings is True and the input is a string
def test_is_sequence_include_strings(mock_is_string):
    mock_is_string.return_value = False
    assert is_sequence('string', include_strings=True)
    # No need to assert mock_is_string.assert_not_called() because is_string is not called when include_strings is True

# Test to cover the case when the input is a non-string sequence
def test_is_sequence_non_string_sequence(mock_is_string):
    mock_is_string.return_value = False
    assert is_sequence([1, 2, 3], include_strings=False)
    # No need to assert mock_is_string.assert_not_called() because is_string might be called to check if the sequence is a string

# Test to cover the case when the input is not a sequence
def test_is_sequence_not_a_sequence(mock_is_string):
    mock_is_string.return_value = False
    assert not is_sequence(123, include_strings=False)
    # No need to assert mock_is_string.assert_not_called() because is_string might be called to check if the non-sequence is a string
