# file: lib/ansible/module_utils/facts/system/distribution.py:19-27
# asked: {"lines": [19, 20, 21, 22, 23, 24, 25, 26, 27], "branches": [[20, 21], [20, 22], [25, 26], [25, 27]]}
# gained: {"lines": [19, 20, 21, 22, 23, 24, 25, 26, 27], "branches": [[20, 21], [20, 22], [25, 26], [25, 27]]}

import pytest
from unittest.mock import Mock

# Assuming the get_uname function is imported from the module
from ansible.module_utils.facts.system.distribution import get_uname

def test_get_uname_with_string_flag():
    module = Mock()
    module.run_command = Mock(return_value=(0, 'Linux version', ''))
    
    result = get_uname(module, '-a')
    
    module.run_command.assert_called_once_with(['uname', '-a'])
    assert result == 'Linux version'

def test_get_uname_with_list_flag():
    module = Mock()
    module.run_command = Mock(return_value=(0, 'Linux version', ''))
    
    result = get_uname(module, ['-a'])
    
    module.run_command.assert_called_once_with(['uname', '-a'])
    assert result == 'Linux version'

def test_get_uname_command_failure():
    module = Mock()
    module.run_command = Mock(return_value=(1, '', 'error'))
    
    result = get_uname(module, '-a')
    
    module.run_command.assert_called_once_with(['uname', '-a'])
    assert result is None
