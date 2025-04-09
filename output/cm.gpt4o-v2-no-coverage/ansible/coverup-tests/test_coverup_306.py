# file: lib/ansible/modules/apt_repository.py:174-186
# asked: {"lines": [174, 176, 177, 178, 179, 180, 181, 182, 183, 184, 186], "branches": [[176, 177], [176, 186], [178, 0], [178, 179], [180, 181], [180, 182], [183, 0], [183, 184]]}
# gained: {"lines": [174, 176, 177, 178, 179, 180, 181, 182, 183, 184, 186], "branches": [[176, 177], [176, 186], [178, 179], [180, 181], [180, 182], [183, 0], [183, 184]]}

import pytest
from unittest.mock import MagicMock

def test_install_python_apt_success(monkeypatch):
    module = MagicMock()
    module.check_mode = False
    module.get_bin_path.return_value = '/usr/bin/apt-get'
    module.run_command.side_effect = [(0, '', ''), (0, '', '')]

    from ansible.modules.apt_repository import install_python_apt
    install_python_apt(module, 'python-apt')

    module.get_bin_path.assert_called_once_with('apt-get')
    assert module.run_command.call_count == 2
    module.run_command.assert_any_call(['/usr/bin/apt-get', 'update'])
    module.run_command.assert_any_call(['/usr/bin/apt-get', 'install', 'python-apt', '-y', '-q'])

def test_install_python_apt_update_fail(monkeypatch):
    module = MagicMock()
    module.check_mode = False
    module.get_bin_path.return_value = '/usr/bin/apt-get'
    module.run_command.side_effect = [(1, '', 'update error')]

    from ansible.modules.apt_repository import install_python_apt
    module.fail_json.side_effect = SystemExit
    with pytest.raises(SystemExit):
        install_python_apt(module, 'python-apt')

    module.get_bin_path.assert_called_once_with('apt-get')
    module.run_command.assert_called_once_with(['/usr/bin/apt-get', 'update'])
    module.fail_json.assert_called_once_with(msg="Failed to auto-install python-apt. Error was: 'update error'")

def test_install_python_apt_install_fail(monkeypatch):
    module = MagicMock()
    module.check_mode = False
    module.get_bin_path.return_value = '/usr/bin/apt-get'
    module.run_command.side_effect = [(0, '', ''), (1, '', 'install error')]

    from ansible.modules.apt_repository import install_python_apt
    module.fail_json.side_effect = SystemExit
    with pytest.raises(SystemExit):
        install_python_apt(module, 'python-apt')

    module.get_bin_path.assert_called_once_with('apt-get')
    assert module.run_command.call_count == 2
    module.run_command.assert_any_call(['/usr/bin/apt-get', 'update'])
    module.run_command.assert_any_call(['/usr/bin/apt-get', 'install', 'python-apt', '-y', '-q'])
    module.fail_json.assert_called_once_with(msg="Failed to auto-install python-apt. Error was: 'install error'")

def test_install_python_apt_check_mode(monkeypatch):
    module = MagicMock()
    module.check_mode = True

    from ansible.modules.apt_repository import install_python_apt
    module.fail_json.side_effect = SystemExit
    with pytest.raises(SystemExit):
        install_python_apt(module, 'python-apt')

    module.fail_json.assert_called_once_with(msg="python-apt must be installed to use check mode")
