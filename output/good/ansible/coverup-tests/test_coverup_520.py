# file lib/ansible/modules/dnf.py:416-430
# lines [416, 422, 423, 424, 426, 430]
# branches ['422->426', '422->430']

import pytest
from ansible.modules.dnf import DnfModule
from ansible.module_utils._text import to_native

class MockYumDnf:
    def __init__(self, module):
        pass

class MockDnfModule(DnfModule, MockYumDnf):
    def __init__(self, module):
        MockYumDnf.__init__(self, module)

@pytest.fixture
def dnf_module(mocker):
    module_mock = mocker.MagicMock()
    mocker.patch('ansible.modules.dnf.YumDnf', MockYumDnf)
    return MockDnfModule(module_mock)

def test_sanitize_dnf_error_msg_remove_no_package_matched(dnf_module):
    spec = 'dummy-package'
    error = 'no package matched'
    is_failure, msg = dnf_module._sanitize_dnf_error_msg_remove(spec, error)
    assert not is_failure
    assert msg == 'dummy-package is not installed'

def test_sanitize_dnf_error_msg_remove_no_match_for_argument(dnf_module):
    spec = 'dummy-package'
    error = 'No match for argument: dummy-package'
    is_failure, msg = dnf_module._sanitize_dnf_error_msg_remove(spec, error)
    assert not is_failure
    assert msg == 'dummy-package is not installed'

def test_sanitize_dnf_error_msg_remove_other_error(dnf_module):
    spec = 'dummy-package'
    error = 'Some other error'
    is_failure, msg = dnf_module._sanitize_dnf_error_msg_remove(spec, error)
    assert is_failure
    assert msg == 'Some other error'
