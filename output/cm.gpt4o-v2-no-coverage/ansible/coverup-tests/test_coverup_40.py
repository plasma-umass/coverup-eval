# file: lib/ansible/module_utils/common/locale.py:10-57
# asked: {"lines": [10, 23, 24, 25, 26, 28, 30, 32, 35, 37, 39, 40, 41, 43, 45, 47, 48, 49, 50, 51, 53, 54, 55, 57], "branches": [[26, 28], [26, 30], [32, 35], [32, 37], [39, 40], [39, 45], [40, 41], [40, 43], [47, 48], [47, 57], [48, 49], [48, 57], [49, 48], [49, 50], [54, 55], [54, 57]]}
# gained: {"lines": [10, 23, 24, 25, 26, 28, 30, 32, 35, 37, 39, 40, 41, 43, 45, 47, 48, 49, 50, 51, 53, 54, 55, 57], "branches": [[26, 28], [26, 30], [32, 35], [32, 37], [39, 40], [39, 45], [40, 41], [40, 43], [47, 48], [48, 49], [49, 48], [49, 50], [54, 55], [54, 57]]}

import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.common.locale import get_best_parsable_locale

@pytest.fixture
def mock_module():
    module = Mock()
    module.get_bin_path = Mock(return_value='/usr/bin/locale')
    module.run_command = Mock(return_value=(0, 'C.utf8\nen_US.utf8\nC\nPOSIX\n', ''))
    return module

def test_get_best_parsable_locale_default(mock_module):
    result = get_best_parsable_locale(mock_module)
    assert result == 'C.utf8'

def test_get_best_parsable_locale_with_preferences(mock_module):
    preferences = ['en_GB.utf8', 'en_US.utf8']
    result = get_best_parsable_locale(mock_module, preferences=preferences)
    assert result == 'en_US.utf8'

def test_get_best_parsable_locale_no_locale_tool():
    module = Mock()
    module.get_bin_path = Mock(return_value=None)
    result = get_best_parsable_locale(module)
    assert result == 'C'

def test_get_best_parsable_locale_no_output(mock_module):
    mock_module.run_command = Mock(return_value=(0, '', ''))
    result = get_best_parsable_locale(mock_module)
    assert result == 'C'

def test_get_best_parsable_locale_command_failure(mock_module):
    mock_module.run_command = Mock(return_value=(1, '', 'error'))
    result = get_best_parsable_locale(mock_module)
    assert result == 'C'

def test_get_best_parsable_locale_raise_on_locale(mock_module):
    mock_module.run_command = Mock(return_value=(1, '', 'error'))
    with pytest.raises(RuntimeWarning):
        get_best_parsable_locale(mock_module, raise_on_locale=True)
