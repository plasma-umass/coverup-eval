# file: lib/ansible/module_utils/common/locale.py:10-57
# asked: {"lines": [10, 23, 24, 25, 26, 28, 30, 32, 35, 37, 39, 40, 41, 43, 45, 47, 48, 49, 50, 51, 53, 54, 55, 57], "branches": [[26, 28], [26, 30], [32, 35], [32, 37], [39, 40], [39, 45], [40, 41], [40, 43], [47, 48], [47, 57], [48, 49], [48, 57], [49, 48], [49, 50], [54, 55], [54, 57]]}
# gained: {"lines": [10, 23, 24, 25, 26, 28, 30, 32, 35, 37, 39, 40, 41, 43, 45, 47, 48, 49, 50, 51, 53, 54, 55, 57], "branches": [[26, 28], [26, 30], [32, 35], [32, 37], [39, 40], [39, 45], [40, 41], [40, 43], [47, 48], [48, 49], [48, 57], [49, 48], [49, 50], [54, 55]]}

import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.common.locale import get_best_parsable_locale

@pytest.fixture
def mock_module():
    return Mock()

def test_get_best_parsable_locale_no_locale_tool(mock_module):
    mock_module.get_bin_path.return_value = None
    with pytest.raises(RuntimeWarning, match="Could not find 'locale' tool"):
        get_best_parsable_locale(mock_module, raise_on_locale=True)

def test_get_best_parsable_locale_no_output(mock_module):
    mock_module.get_bin_path.return_value = "/usr/bin/locale"
    mock_module.run_command.return_value = (0, "", "error")
    with pytest.raises(RuntimeWarning, match="No output from locale, rc=0: error"):
        get_best_parsable_locale(mock_module, raise_on_locale=True)

def test_get_best_parsable_locale_unable_to_get_info(mock_module):
    mock_module.get_bin_path.return_value = "/usr/bin/locale"
    mock_module.run_command.return_value = (1, "", "error")
    with pytest.raises(RuntimeWarning, match="Unable to get locale information, rc=1: error"):
        get_best_parsable_locale(mock_module, raise_on_locale=True)

def test_get_best_parsable_locale_preferences_none(mock_module):
    mock_module.get_bin_path.return_value = "/usr/bin/locale"
    mock_module.run_command.return_value = (0, "C.utf8\nen_US.utf8\nC\nPOSIX", "")
    result = get_best_parsable_locale(mock_module)
    assert result == 'C.utf8'

def test_get_best_parsable_locale_with_preferences(mock_module):
    mock_module.get_bin_path.return_value = "/usr/bin/locale"
    mock_module.run_command.return_value = (0, "C.utf8\nen_US.utf8\nC\nPOSIX", "")
    preferences = ['en_GB.utf8', 'en_US.utf8']
    result = get_best_parsable_locale(mock_module, preferences=preferences)
    assert result == 'en_US.utf8'

def test_get_best_parsable_locale_no_matching_preferences(mock_module):
    mock_module.get_bin_path.return_value = "/usr/bin/locale"
    mock_module.run_command.return_value = (0, "fr_FR.utf8\nde_DE.utf8", "")
    preferences = ['en_GB.utf8', 'en_US.utf8']
    result = get_best_parsable_locale(mock_module, preferences=preferences)
    assert result == 'C'
