# file lib/ansible/modules/pip.py:396-452
# lines [401, 402, 404, 406, 407, 408, 409, 413, 414, 418, 420, 421, 422, 423, 424, 425, 426, 430, 431, 435, 436, 437, 438, 439, 440, 441, 445, 446, 447, 449, 450, 452]
# branches ['402->404', '402->406', '407->408', '407->414', '408->409', '408->413', '414->418', '414->420', '420->421', '420->449', '421->422', '421->435', '423->424', '423->430', '425->423', '425->426', '437->438', '437->445', '439->437', '439->440', '449->450', '449->452']

import os
import sys
import pytest
from unittest import mock

# Mocking the module and its methods
class MockModule:
    def get_bin_path(self, name, required, opt_dirs):
        return None

    def fail_json(self, msg):
        raise Exception(msg)

@pytest.fixture
def mock_module():
    return MockModule()

@pytest.fixture
def mock_os_path_isabs(mocker):
    return mocker.patch('os.path.isabs', return_value=False)

@pytest.fixture
def mock_os_path_exists(mocker):
    return mocker.patch('os.path.exists', return_value=False)

@pytest.fixture
def mock_is_executable(mocker):
    return mocker.patch('ansible.modules.pip.is_executable', return_value=False)

@pytest.fixture
def mock_have_pip_module(mocker):
    return mocker.patch('ansible.modules.pip._have_pip_module', return_value=False)

@pytest.fixture
def mock_sys_executable(mocker):
    return mocker.patch('sys.executable', '/usr/bin/python')

def test_get_pip_no_executable_no_env(mock_module, mock_os_path_isabs, mock_os_path_exists, mock_is_executable, mock_have_pip_module, mock_sys_executable):
    from ansible.modules.pip import _get_pip, PY3

    # Determine the expected pip basenames based on Python version
    expected_pip_basenames = ('pip3',) if PY3 else ('pip2', 'pip')

    # Test when no executable and no env are provided
    with pytest.raises(Exception, match=f'Unable to find any of {", ".join(expected_pip_basenames)} to use.  pip needs to be installed.'):
        _get_pip(mock_module)

    # Test when no executable and env is provided
    expected_virtualenv_basenames = ('pip3', 'pip') if PY3 else ('pip2', 'pip')
    with pytest.raises(Exception, match=f'Unable to find pip in the virtualenv, /fake_env, under any of these names: {", ".join(expected_virtualenv_basenames)}. Make sure pip is present in the virtualenv.'):
        _get_pip(mock_module, env='/fake_env')

    # Test when executable is provided but not absolute
    with pytest.raises(Exception, match='Unable to find any of fake_executable to use.  pip needs to be installed.'):
        _get_pip(mock_module, executable='fake_executable')

    # Test when executable is provided and absolute
    mock_os_path_isabs.return_value = True
    result = _get_pip(mock_module, executable='/usr/bin/pip')
    assert result == ['/usr/bin/pip']

    # Test when _have_pip_module returns True
    mock_have_pip_module.return_value = True
    result = _get_pip(mock_module)
    assert result == ['/usr/bin/python', '-m', 'pip.__main__']

    # Test when PY3 is True
    if PY3:
        result = _get_pip(mock_module)
        assert result == ['/usr/bin/python', '-m', 'pip.__main__']

    # Test when env is provided and pip is found in virtualenv
    mock_os_path_exists.return_value = True
    mock_is_executable.return_value = True
    result = _get_pip(mock_module, env='/fake_env')
    assert result == ['/fake_env/bin/pip3'] if PY3 else ['/fake_env/bin/pip2']

    # Test when env is provided and pip is not found in virtualenv
    mock_os_path_exists.return_value = False
    with pytest.raises(Exception, match=f'Unable to find pip in the virtualenv, /fake_env, under any of these names: {", ".join(expected_virtualenv_basenames)}. Make sure pip is present in the virtualenv.'):
        _get_pip(mock_module, env='/fake_env')
