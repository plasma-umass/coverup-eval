# file lib/ansible/module_utils/common/locale.py:10-57
# lines []
# branches ['47->57', '48->57']

import pytest
from unittest.mock import Mock

# Assuming the function is imported from the module
from ansible.module_utils.common.locale import get_best_parsable_locale

def test_get_best_parsable_locale_no_available_locales(mocker):
    module = Mock()
    module.get_bin_path.return_value = "/usr/bin/locale"
    module.run_command.return_value = (0, "", "")

    result = get_best_parsable_locale(module, raise_on_locale=False)
    assert result == 'C'

def test_get_best_parsable_locale_raise_on_locale(mocker):
    module = Mock()
    module.get_bin_path.return_value = "/usr/bin/locale"
    module.run_command.return_value = (0, "", "")

    with pytest.raises(RuntimeWarning):
        get_best_parsable_locale(module, raise_on_locale=True)

def test_get_best_parsable_locale_with_available_locales(mocker):
    module = Mock()
    module.get_bin_path.return_value = "/usr/bin/locale"
    module.run_command.return_value = (0, "C.utf8\nen_US.utf8\nC\nPOSIX\n", "")

    result = get_best_parsable_locale(module, raise_on_locale=False)
    assert result == 'C.utf8'

def test_get_best_parsable_locale_with_no_matching_locales(mocker):
    module = Mock()
    module.get_bin_path.return_value = "/usr/bin/locale"
    module.run_command.return_value = (0, "fr_FR.utf8\nde_DE.utf8\n", "")

    result = get_best_parsable_locale(module, raise_on_locale=False)
    assert result == 'C'
