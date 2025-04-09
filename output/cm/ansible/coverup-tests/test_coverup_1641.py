# file lib/ansible/modules/dnf.py:403-414
# lines [408, 409, 410, 412, 414]
# branches ['408->412', '408->414']

import pytest
from ansible.modules.dnf import DnfModule
from ansible.module_utils._text import to_text

@pytest.fixture
def dnf_module(mocker):
    module_mock = mocker.MagicMock()
    module_mock.run_command.return_value = (0, 'en_US.utf8\nC.utf8\nC\nPOSIX', '')
    mocker.patch('ansible.modules.dnf.YumDnf', return_value=module_mock)
    mocker.patch('ansible.modules.dnf.get_best_parsable_locale', return_value='C')
    return DnfModule(module=module_mock)

def test_sanitize_dnf_error_msg_install_no_package_matched(dnf_module):
    spec = 'nonexistent-package'
    error = "Error: no package matched"
    sanitized_error = dnf_module._sanitize_dnf_error_msg_install(spec, error)
    assert sanitized_error == "No package nonexistent-package available."

def test_sanitize_dnf_error_msg_install_no_match_for_argument(dnf_module):
    spec = 'nonexistent-package'
    error = "Error: No match for argument: nonexistent-package"
    sanitized_error = dnf_module._sanitize_dnf_error_msg_install(spec, error)
    assert sanitized_error == "No package nonexistent-package available."

def test_sanitize_dnf_error_msg_install_other_error(dnf_module):
    spec = 'existent-package'
    error = "Error: Some other error"
    sanitized_error = dnf_module._sanitize_dnf_error_msg_install(spec, error)
    assert sanitized_error == error
