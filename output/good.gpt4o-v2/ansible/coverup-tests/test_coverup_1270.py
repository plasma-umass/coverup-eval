# file: lib/ansible/module_utils/common/locale.py:10-57
# asked: {"lines": [], "branches": [[47, 57], [54, 57]]}
# gained: {"lines": [], "branches": [[54, 57]]}

import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.common.locale import get_best_parsable_locale

@pytest.fixture
def mock_module():
    return Mock()

def test_get_best_parsable_locale_no_locale_tool(mock_module):
    mock_module.get_bin_path.return_value = None
    assert get_best_parsable_locale(mock_module) == 'C'

def test_get_best_parsable_locale_no_output(mock_module):
    mock_module.get_bin_path.return_value = '/usr/bin/locale'
    mock_module.run_command.return_value = (0, '', 'error')
    assert get_best_parsable_locale(mock_module) == 'C'

def test_get_best_parsable_locale_unable_to_get_locale_info(mock_module):
    mock_module.get_bin_path.return_value = '/usr/bin/locale'
    mock_module.run_command.return_value = (1, '', 'error')
    assert get_best_parsable_locale(mock_module) == 'C'

def test_get_best_parsable_locale_with_available_locales(mock_module):
    mock_module.get_bin_path.return_value = '/usr/bin/locale'
    mock_module.run_command.return_value = (0, 'C.utf8\nen_US.utf8\nC\nPOSIX\n', '')
    assert get_best_parsable_locale(mock_module) == 'C.utf8'

def test_get_best_parsable_locale_raise_on_locale(mock_module):
    mock_module.get_bin_path.return_value = None
    with pytest.raises(RuntimeWarning):
        get_best_parsable_locale(mock_module, raise_on_locale=True)
