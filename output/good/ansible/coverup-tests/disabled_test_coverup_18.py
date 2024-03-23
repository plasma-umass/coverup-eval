# file lib/ansible/playbook/base.py:83-119
# lines [83, 84, 85, 86, 87, 91, 93, 94, 96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]
# branches ['96->97', '96->99', '99->100', '99->117', '100->101', '100->102', '102->103', '102->105', '106->107', '106->108', '109->110', '109->115', '110->111', '110->112', '113->109', '113->114', '115->116', '115->117', '117->exit', '117->118']

import pytest
from ansible.playbook.base import _validate_action_group_metadata
from ansible.utils.display import Display
from ansible import constants as C

# Mock the display object to capture warnings
@pytest.fixture
def mock_display(mocker):
    display_mock = mocker.patch.object(Display, 'warning')
    return display_mock

# Test function to cover missing lines/branches
def test_validate_action_group_metadata(mock_display):
    # Set the constant to enable validation
    C.VALIDATE_ACTION_GROUP_METADATA = True

    # Test case with an action that is not only metadata
    action_with_extra_keys = {'metadata': {}, 'name': 'test'}
    fq_group_name = 'test_group'
    _validate_action_group_metadata(action_with_extra_keys, False, fq_group_name)
    mock_display.assert_called_once()
    mock_display.reset_mock()

    # Test case with multiple metadata entries
    _validate_action_group_metadata({'metadata': {}}, True, fq_group_name)
    mock_display.assert_called_once()
    mock_display.reset_mock()

    # Test case with metadata not being a dictionary
    _validate_action_group_metadata({'metadata': []}, False, fq_group_name)
    mock_display.assert_called_once()
    mock_display.reset_mock()

    # Test case with unexpected keys in metadata
    action_with_unexpected_keys = {'metadata': {'unexpected_key': 'value'}}
    _validate_action_group_metadata(action_with_unexpected_keys, False, fq_group_name)
    mock_display.assert_called_once()
    mock_display.reset_mock()

    # Test case with unexpected key types in metadata
    action_with_unexpected_types = {'metadata': {'extend_group': 123}}
    _validate_action_group_metadata(action_with_unexpected_types, False, fq_group_name)
    mock_display.assert_called_once()
    mock_display.reset_mock()

    # Test case with valid metadata
    action_with_valid_metadata = {'metadata': {'extend_group': ['valid_list']}}
    _validate_action_group_metadata(action_with_valid_metadata, False, fq_group_name)
    mock_display.assert_not_called()

    # Reset the constant to its original value
    C.VALIDATE_ACTION_GROUP_METADATA = False
