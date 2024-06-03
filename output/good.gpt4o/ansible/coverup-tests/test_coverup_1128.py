# file lib/ansible/modules/pip.py:363-378
# lines [366, 367, 368, 369, 372, 373, 374, 375, 376, 378]
# branches ['372->373', '372->378', '375->376', '375->378']

import pytest
from unittest import mock
from ansible.modules.pip import _get_packages

@pytest.fixture
def mock_module():
    module = mock.Mock()
    module.run_command = mock.Mock()
    return module

@pytest.fixture
def mock_pip():
    return ['pip']

@pytest.fixture
def mock_chdir():
    return '/some/directory'

@pytest.fixture
def mock_locale(mocker):
    mocker.patch('ansible.modules.pip.get_best_parsable_locale', return_value='en_US.UTF-8')

def test_get_packages_pip_list_fails_pip_freeze_succeeds(mock_module, mock_pip, mock_chdir, mock_locale):
    # Simulate 'pip list' command failure
    mock_module.run_command.side_effect = [
        (1, '', 'error'),  # First call to 'pip list' fails
        (0, 'package==1.0.0\n', '')  # Second call to 'pip freeze' succeeds
    ]

    command, out, err = _get_packages(mock_module, mock_pip, mock_chdir)

    # Verify the correct commands were run
    assert mock_module.run_command.call_count == 2
    assert mock_module.run_command.call_args_list[0][0][0] == ['pip', 'list', '--format=freeze']
    assert mock_module.run_command.call_args_list[1][0][0] == ['pip', 'freeze']

    # Verify the output
    assert command == 'pip freeze'
    assert out == 'package==1.0.0\n'
    assert err == ''

def test_get_packages_pip_list_and_freeze_fail(mock_module, mock_pip, mock_chdir, mock_locale):
    # Simulate both 'pip list' and 'pip freeze' command failures
    mock_module.run_command.side_effect = [
        (1, '', 'error'),  # First call to 'pip list' fails
        (1, '', 'error')  # Second call to 'pip freeze' also fails
    ]

    with mock.patch('ansible.modules.pip._fail', side_effect=SystemExit) as mock_fail:
        with pytest.raises(SystemExit):
            _get_packages(mock_module, mock_pip, mock_chdir)

        # Verify the correct commands were run
        assert mock_module.run_command.call_count == 2
        assert mock_module.run_command.call_args_list[0][0][0] == ['pip', 'list', '--format=freeze']
        assert mock_module.run_command.call_args_list[1][0][0] == ['pip', 'freeze']

        # Verify _fail was called
        assert mock_fail.call_count == 1
