# file lib/ansible/module_utils/common/locale.py:10-57
# lines [10, 23, 24, 25, 26, 28, 30, 32, 35, 37, 39, 40, 41, 43, 45, 47, 48, 49, 50, 51, 53, 54, 55, 57]
# branches ['26->28', '26->30', '32->35', '32->37', '39->40', '39->45', '40->41', '40->43', '47->48', '47->57', '48->49', '48->57', '49->48', '49->50', '54->55', '54->57']

import pytest
from ansible.module_utils.common.locale import get_best_parsable_locale
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_native

def test_get_best_parsable_locale(mocker):
    # Mocking AnsibleModule instance
    module_mock = mocker.MagicMock(spec=AnsibleModule)
    module_mock.get_bin_path.return_value = '/usr/bin/locale'
    module_mock.run_command.return_value = (0, 'C.utf8\nen_US.utf8\nC\nPOSIX', '')

    # Test with default preferences
    assert get_best_parsable_locale(module_mock) == 'C.utf8'

    # Test with custom preferences
    assert get_best_parsable_locale(module_mock, preferences=['en_GB.utf8', 'C']) == 'C'

    # Test with no 'locale' tool available
    module_mock.get_bin_path.return_value = None
    with pytest.raises(RuntimeWarning):
        get_best_parsable_locale(module_mock, raise_on_locale=True)

    # Test with 'locale' tool available but no output
    module_mock.get_bin_path.return_value = '/usr/bin/locale'
    module_mock.run_command.return_value = (0, '', '')
    with pytest.raises(RuntimeWarning):
        get_best_parsable_locale(module_mock, raise_on_locale=True)

    # Test with 'locale' tool available but non-zero return code
    module_mock.run_command.return_value = (1, '', 'error')
    with pytest.raises(RuntimeWarning):
        get_best_parsable_locale(module_mock, raise_on_locale=True)

    # Test with 'locale' tool available, non-zero return code, but not raising
    assert get_best_parsable_locale(module_mock, raise_on_locale=False) == 'C'

    # Cleanup after test
    mocker.stopall()
