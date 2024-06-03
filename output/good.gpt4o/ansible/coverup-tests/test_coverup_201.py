# file lib/ansible/modules/apt_repository.py:174-186
# lines [174, 176, 177, 178, 179, 180, 181, 182, 183, 184, 186]
# branches ['176->177', '176->186', '178->exit', '178->179', '180->181', '180->182', '183->exit', '183->184']

import pytest
from unittest.mock import Mock

def test_install_python_apt(mocker):
    module = Mock()
    module.check_mode = False
    module.get_bin_path.return_value = '/usr/bin/apt-get'
    module.run_command.side_effect = [
        (0, 'update output', ''),
        (0, 'install output', '')
    ]
    
    def fail_json(msg):
        raise Exception(msg)
    
    module.fail_json = fail_json
    
    from ansible.modules.apt_repository import install_python_apt
    
    # Test successful installation
    install_python_apt(module, 'python-apt')
    module.get_bin_path.assert_called_with('apt-get')
    module.run_command.assert_any_call(['/usr/bin/apt-get', 'update'])
    module.run_command.assert_any_call(['/usr/bin/apt-get', 'install', 'python-apt', '-y', '-q'])
    
    # Test failure on update
    module.run_command.side_effect = [
        (1, '', 'update error')
    ]
    with pytest.raises(Exception, match="Failed to auto-install python-apt. Error was: 'update error'"):
        install_python_apt(module, 'python-apt')
    
    # Test failure on install
    module.run_command.side_effect = [
        (0, 'update output', ''),
        (1, '', 'install error')
    ]
    with pytest.raises(Exception, match="Failed to auto-install python-apt. Error was: 'install error'"):
        install_python_apt(module, 'python-apt')
    
    # Test check mode
    module.check_mode = True
    with pytest.raises(Exception, match="python-apt must be installed to use check mode"):
        install_python_apt(module, 'python-apt')
