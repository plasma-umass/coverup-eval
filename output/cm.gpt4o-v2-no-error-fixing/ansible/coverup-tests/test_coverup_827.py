# file: lib/ansible/module_utils/common/locale.py:10-57
# asked: {"lines": [], "branches": [[47, 57], [54, 57]]}
# gained: {"lines": [], "branches": [[54, 57]]}

import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.common.locale import get_best_parsable_locale

@pytest.fixture
def mock_module():
    module = Mock()
    module.get_bin_path = Mock(return_value='/usr/bin/locale')
    return module

def test_get_best_parsable_locale_no_available_locales(mock_module):
    mock_module.run_command = Mock(return_value=(0, '', ''))
    result = get_best_parsable_locale(mock_module)
    assert result == 'C'

def test_get_best_parsable_locale_with_preferences(mock_module):
    mock_module.run_command = Mock(return_value=(0, 'C.utf8\nen_US.utf8\nC\nPOSIX\n', ''))
    result = get_best_parsable_locale(mock_module, preferences=['en_US.utf8', 'C.utf8'])
    assert result == 'en_US.utf8'

def test_get_best_parsable_locale_raise_on_locale(mock_module):
    mock_module.run_command = Mock(return_value=(1, '', 'error'))
    with pytest.raises(RuntimeWarning):
        get_best_parsable_locale(mock_module, raise_on_locale=True)

def test_get_best_parsable_locale_no_locale_tool(mock_module):
    mock_module.get_bin_path = Mock(return_value=None)
    with pytest.raises(RuntimeWarning):
        get_best_parsable_locale(mock_module, raise_on_locale=True)
