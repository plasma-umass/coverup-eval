# file lib/ansible/modules/pip.py:363-378
# lines [363, 366, 367, 368, 369, 372, 373, 374, 375, 376, 378]
# branches ['372->373', '372->378', '375->376', '375->378']

import pytest
from ansible.modules.pip import _get_packages

class FakeModule:
    def run_command(self, command, cwd=None, environ_update=None):
        if 'list' in command:
            return 1, '', 'ERROR: pip list failed'
        elif 'freeze' in command:
            return 0, 'package==1.0.0', ''
        else:
            return 1, '', 'ERROR: Unknown command'

    def fail_json(self, msg):
        raise Exception("Module failed. Msg: {}".format(msg))

def _fail(module, command, out, err):
    module.fail_json(msg="Command {} failed with output: {}, error: {}".format(command, out, err))

@pytest.fixture
def mock_module(mocker):
    module = FakeModule()
    mocker.patch('ansible.modules.pip.get_best_parsable_locale', return_value='en_US.UTF-8')
    mocker.patch('ansible.modules.pip._fail', side_effect=_fail)
    return module

def test_get_packages_with_fallback_to_freeze(mock_module):
    pip_command = ['pip']
    chdir = '/fake/dir'
    command, out, err = _get_packages(mock_module, pip_command, chdir)
    assert command == 'pip freeze'
    assert out == 'package==1.0.0'
    assert err == ''
