# file lib/ansible/constants.py:48-60
# lines [48, 49, 50, 51, 52, 54, 55, 56, 58, 59, 60]
# branches []

import pytest
from ansible.constants import _DeprecatedSequenceConstant

# Mocking the _deprecated function to avoid side effects
def test_deprecated_sequence_constant(mocker):
    # Arrange
    mock_deprecated = mocker.patch('ansible.constants._deprecated')
    test_sequence = _DeprecatedSequenceConstant([1, 2, 3], 'deprecated message', '2.0')

    # Act and Assert for __len__
    assert len(test_sequence) == 3
    mock_deprecated.assert_called_once_with('deprecated message', '2.0')
    mock_deprecated.reset_mock()

    # Act and Assert for __getitem__
    assert test_sequence[1] == 2
    mock_deprecated.assert_called_once_with('deprecated message', '2.0')
