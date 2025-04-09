# file lib/ansible/playbook/base.py:83-119
# lines [84, 85, 86, 87, 91, 93, 94, 96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]
# branches ['96->97', '96->99', '99->100', '99->117', '100->101', '100->102', '102->103', '102->105', '106->107', '106->108', '109->110', '109->115', '110->111', '110->112', '113->109', '113->114', '115->116', '115->117', '117->exit', '117->118']

import pytest
from ansible.playbook.base import _validate_action_group_metadata
from ansible.utils.display import Display
from ansible import constants as C

# Mock the Display class to capture warnings
@pytest.fixture
def mock_display(mocker):
    return mocker.patch.object(Display, 'warning')

# Test function to cover lines 84-119
def test_validate_action_group_metadata(mock_display):
    # Set the constant to enable validation
    C.VALIDATE_ACTION_GROUP_METADATA = True

    # Test case with non-metadata-only dictionary and multiple metadata entries
    action = {'name': 'test', 'metadata': {}}
    _validate_action_group_metadata(action, True, 'test_group')
    assert mock_display.call_count == 1
    mock_display.reset_mock()

    # Test case with non-dictionary metadata
    action = {'metadata': 'not a dict'}
    _validate_action_group_metadata(action, False, 'test_group')
    assert mock_display.call_count == 1
    mock_display.reset_mock()

    # Test case with unexpected keys in metadata
    action = {'metadata': {'unexpected_key': 'value'}}
    _validate_action_group_metadata(action, False, 'test_group')
    assert mock_display.call_count == 1
    mock_display.reset_mock()

    # Test case with unexpected key types in metadata
    action = {'metadata': {'extend_group': 123}}
    _validate_action_group_metadata(action, False, 'test_group')
    assert mock_display.call_count == 1
    mock_display.reset_mock()

    # Test case with correct metadata
    action = {'metadata': {'extend_group': ['correct_type']}}
    _validate_action_group_metadata(action, False, 'test_group')
    assert mock_display.call_count == 0

    # Reset the constant to its original value
    C.VALIDATE_ACTION_GROUP_METADATA = False
