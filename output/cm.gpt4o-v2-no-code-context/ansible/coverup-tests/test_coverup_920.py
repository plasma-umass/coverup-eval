# file: lib/ansible/module_utils/common/locale.py:10-57
# asked: {"lines": [23, 24, 25, 26, 28, 30, 32, 35, 37, 39, 40, 41, 43, 45, 47, 48, 49, 50, 51, 53, 54, 55, 57], "branches": [[26, 28], [26, 30], [32, 35], [32, 37], [39, 40], [39, 45], [40, 41], [40, 43], [47, 48], [47, 57], [48, 49], [48, 57], [49, 48], [49, 50], [54, 55], [54, 57]]}
# gained: {"lines": [23, 24, 25, 26, 28, 30, 32, 35, 37, 39, 40, 41, 43, 45, 47, 48, 49, 50, 51, 53, 54, 55, 57], "branches": [[26, 28], [26, 30], [32, 35], [32, 37], [39, 40], [39, 45], [40, 41], [40, 43], [47, 48], [48, 49], [49, 48], [49, 50], [54, 55], [54, 57]]}

import pytest
from unittest.mock import Mock, patch

# Mock AnsibleModule for testing
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

def test_get_best_parsable_locale_default(module):
    from ansible.module_utils.common.locale import get_best_parsable_locale
    result = get_best_parsable_locale(module)
    assert result == 'C.utf8'

def test_get_best_parsable_locale_with_preferences(module):
    from ansible.module_utils.common.locale import get_best_parsable_locale
    preferences = ['en_GB.utf8', 'fr_FR.utf8', 'C.utf8']
    result = get_best_parsable_locale(module, preferences)
    assert result == 'C.utf8'

def test_get_best_parsable_locale_no_locale_tool(module):
    from ansible.module_utils.common.locale import get_best_parsable_locale
    module.get_bin_path = Mock(return_value=None)
    result = get_best_parsable_locale(module)
    assert result == 'C'

def test_get_best_parsable_locale_no_output_from_locale(module):
    from ansible.module_utils.common.locale import get_best_parsable_locale
    module.run_command = Mock(return_value=(0, "", ""))
    result = get_best_parsable_locale(module)
    assert result == 'C'

def test_get_best_parsable_locale_unable_to_get_locale_info(module):
    from ansible.module_utils.common.locale import get_best_parsable_locale
    module.run_command = Mock(return_value=(1, "", "error"))
    result = get_best_parsable_locale(module)
    assert result == 'C'

def test_get_best_parsable_locale_raise_on_locale(module):
    from ansible.module_utils.common.locale import get_best_parsable_locale
    module.get_bin_path = Mock(return_value=None)
    with pytest.raises(RuntimeWarning):
        get_best_parsable_locale(module, raise_on_locale=True)
