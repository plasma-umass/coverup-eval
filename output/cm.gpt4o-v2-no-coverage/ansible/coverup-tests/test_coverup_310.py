# file: lib/ansible/modules/pip.py:363-378
# asked: {"lines": [363, 366, 367, 368, 369, 372, 373, 374, 375, 376, 378], "branches": [[372, 373], [372, 378], [375, 376], [375, 378]]}
# gained: {"lines": [363, 366, 367, 368, 369, 372, 373, 374, 375, 376, 378], "branches": [[372, 373], [375, 376], [375, 378]]}

import pytest
from unittest import mock
from ansible.module_utils.common.locale import get_best_parsable_locale

# Mocking the module and its methods
class MockModule:
    def run_command(self, command, cwd=None, environ_update=None):
        if '--format=freeze' in command:
            return (1, '', 'pip list error')  # Simulate pip list failure
        elif 'freeze' in command:
            return (0, 'package==1.0.0', '')  # Simulate pip freeze success
        return (0, '', '')

    def fail_json(self, **kwargs):
        raise Exception(kwargs)

    def get_bin_path(self, arg):
        return "/usr/bin/locale"

@pytest.fixture
def module():
    return MockModule()

def test_get_packages_pip_list_failure(module):
    from ansible.modules.pip import _get_packages

    pip = ['pip']
    chdir = '/some/path'

    with mock.patch('ansible.module_utils.common.locale.get_best_parsable_locale', return_value='C'):
        command, out, err = _get_packages(module, pip, chdir)

    assert command == 'pip freeze'
    assert out == 'package==1.0.0'
    assert err == ''

def test_get_packages_pip_freeze_failure(module):
    from ansible.modules.pip import _get_packages

    pip = ['pip']
    chdir = '/some/path'

    def run_command_side_effect(command, cwd=None, environ_update=None):
        if 'freeze' in command:
            return (1, '', 'pip freeze error')  # Simulate pip freeze failure
        return (1, '', 'pip list error')  # Simulate pip list failure

    module.run_command = mock.Mock(side_effect=run_command_side_effect)

    with mock.patch('ansible.module_utils.common.locale.get_best_parsable_locale', return_value='C'):
        with pytest.raises(Exception) as excinfo:
            _get_packages(module, pip, chdir)

    assert 'pip freeze error' in str(excinfo.value)
