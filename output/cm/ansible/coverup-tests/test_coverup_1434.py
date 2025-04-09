# file lib/ansible/module_utils/common/locale.py:10-57
# lines []
# branches ['47->57', '48->57']

import pytest
from ansible.module_utils.common.locale import get_best_parsable_locale
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_native

@pytest.fixture
def mock_module(mocker):
    mock_module = mocker.MagicMock(spec=AnsibleModule)
    mock_module.get_bin_path.return_value = '/usr/bin/locale'
    return mock_module

def test_get_best_parsable_locale_with_missing_preferences(mock_module, mocker):
    # Mock the run_command method to return a list of available locales
    mock_module.run_command.return_value = (0, 'C.utf8\nen_US.utf8\nC\nPOSIX', '')

    # Define preferences that include a locale not in the available list
    preferences = ['missing_locale', 'C.utf8']

    # Call the function with the mocked module and the preferences list
    result = get_best_parsable_locale(mock_module, preferences=preferences)

    # Assert that the result is 'C.utf8', which is the first available preference
    assert result == 'C.utf8'

    # Assert that the run_command method was called with the expected arguments
    mock_module.run_command.assert_called_once_with(['/usr/bin/locale', '-a'])

def test_get_best_parsable_locale_with_all_missing_preferences(mock_module, mocker):
    # Mock the run_command method to return a list of available locales
    mock_module.run_command.return_value = (0, 'C.utf8\nen_US.utf8\nC\nPOSIX', '')

    # Define preferences that do not include any of the available locales
    preferences = ['missing_locale1', 'missing_locale2']

    # Call the function with the mocked module and the preferences list
    result = get_best_parsable_locale(mock_module, preferences=preferences)

    # Assert that the result is 'C', which is the default when no preferences match
    assert result == 'C'

    # Assert that the run_command method was called with the expected arguments
    mock_module.run_command.assert_called_once_with(['/usr/bin/locale', '-a'])

def test_get_best_parsable_locale_raise_on_missing_locale_tool(mock_module, mocker):
    # Mock the get_bin_path method to return None, simulating a missing 'locale' tool
    mock_module.get_bin_path.return_value = None

    # Call the function with the mocked module and raise_on_locale set to True
    with pytest.raises(RuntimeWarning) as excinfo:
        get_best_parsable_locale(mock_module, raise_on_locale=True)

    # Assert that the exception message matches the expected warning
    assert "Could not find 'locale' tool" in str(excinfo.value)

    # Assert that the get_bin_path method was called with the expected arguments
    mock_module.get_bin_path.assert_called_once_with("locale")
