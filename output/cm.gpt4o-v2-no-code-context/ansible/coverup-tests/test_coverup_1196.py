# file: lib/ansible/module_utils/common/locale.py:10-57
# asked: {"lines": [], "branches": [[47, 57], [48, 57]]}
# gained: {"lines": [], "branches": [[48, 57]]}

import pytest
from unittest.mock import Mock, patch

# Mock AnsibleModule
class MockModule:
    def get_bin_path(self, command):
        if command == "locale":
            return "/usr/bin/locale"
        return None

    def run_command(self, command):
        if command == ["/usr/bin/locale", "-a"]:
            return (0, "C.utf8\nen_US.utf8\nC\nPOSIX\n", "")
        return (1, "", "error")

@pytest.fixture
def module():
    return MockModule()

def test_get_best_parsable_locale_with_available_locales(module):
    from ansible.module_utils.common.locale import get_best_parsable_locale

    result = get_best_parsable_locale(module)
    assert result == 'C.utf8'

def test_get_best_parsable_locale_no_available_locales(module):
    from ansible.module_utils.common.locale import get_best_parsable_locale

    with patch.object(module, 'run_command', return_value=(0, "", "")):
        result = get_best_parsable_locale(module)
        assert result == 'C'

def test_get_best_parsable_locale_raise_on_locale(module):
    from ansible.module_utils.common.locale import get_best_parsable_locale

    with patch.object(module, 'get_bin_path', return_value=None):
        with pytest.raises(RuntimeWarning):
            get_best_parsable_locale(module, raise_on_locale=True)

def test_get_best_parsable_locale_no_locale_tool(module):
    from ansible.module_utils.common.locale import get_best_parsable_locale

    with patch.object(module, 'get_bin_path', return_value=None):
        result = get_best_parsable_locale(module)
        assert result == 'C'

def test_get_best_parsable_locale_with_empty_preferences(module):
    from ansible.module_utils.common.locale import get_best_parsable_locale

    with patch.object(module, 'run_command', return_value=(0, "C.utf8\nen_US.utf8\nC\nPOSIX\n", "")):
        result = get_best_parsable_locale(module, preferences=[])
        assert result == 'C'

def test_get_best_parsable_locale_with_no_matching_preferences(module):
    from ansible.module_utils.common.locale import get_best_parsable_locale

    with patch.object(module, 'run_command', return_value=(0, "fr_FR.utf8\nde_DE.utf8\n", "")):
        result = get_best_parsable_locale(module, preferences=['es_ES.utf8', 'it_IT.utf8'])
        assert result == 'C'
