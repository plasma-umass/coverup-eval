# file lib/ansible/inventory/group.py:32-53
# lines [39, 40, 41, 42, 43, 44, 46, 47, 48, 51]
# branches ['38->39', '40->41', '40->46', '42->43', '42->50', '46->47', '46->50', '50->51']

import pytest
from ansible.inventory.group import to_safe_group_name
from ansible.utils.display import Display

# Mock the display object to capture its output
@pytest.fixture
def mock_display(mocker):
    return mocker.patch.object(Display, 'vvvv', autospec=True)

@pytest.fixture
def mock_display_warning(mocker):
    return mocker.patch.object(Display, 'warning', autospec=True)

# Test function to cover lines 39-48, 51
def test_to_safe_group_name_invalid_chars(mock_display, mock_display_warning, mocker):
    # Mock the C global configuration object
    mock_C = mocker.patch('ansible.inventory.group.C')
    mock_C.TRANSFORM_INVALID_GROUP_CHARS = 'always'
    mock_C.INVALID_VARIABLE_NAMES.findall.return_value = [':']
    mock_C.INVALID_VARIABLE_NAMES.sub.return_value = 'invalid_name'

    # Call the function with a name containing invalid characters
    result = to_safe_group_name('invalid:name', force=True)
    # Check that the invalid characters are replaced
    assert result == 'invalid_name'
    # Check that the warning was displayed
    mock_display.assert_called_once()
    mock_display_warning.assert_called_once()

    # Reset the mock
    mock_display.reset_mock()
    mock_display_warning.reset_mock()

    # Set the configuration to never replace invalid characters
    mock_C.TRANSFORM_INVALID_GROUP_CHARS = 'never'
    # Call the function with a name containing invalid characters
    result = to_safe_group_name('invalid:name', force=False)
    # Check that the invalid characters are not replaced
    assert result == 'invalid:name'
    # Check that the warning was displayed
    mock_display.assert_called_once()
    mock_display_warning.assert_called_once()

    # Reset the mock
    mock_display.reset_mock()
    mock_display_warning.reset_mock()

    # Set the configuration to ignore invalid characters
    mock_C.TRANSFORM_INVALID_GROUP_CHARS = 'ignore'
    # Call the function with a name containing invalid characters
    result = to_safe_group_name('invalid:name', force=False)
    # Check that the invalid characters are not replaced
    assert result == 'invalid:name'
    # Check that the warning was not displayed
    mock_display.assert_not_called()
    mock_display_warning.assert_not_called()
