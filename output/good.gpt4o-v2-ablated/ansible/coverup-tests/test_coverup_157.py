# file: lib/ansible/module_utils/facts/system/distribution.py:19-27
# asked: {"lines": [19, 20, 21, 22, 23, 24, 25, 26, 27], "branches": [[20, 21], [20, 22], [25, 26], [25, 27]]}
# gained: {"lines": [19, 20, 21, 22, 23, 24, 25, 26, 27], "branches": [[20, 21], [20, 22], [25, 26], [25, 27]]}

import pytest
from unittest.mock import Mock

def test_get_uname_success(monkeypatch):
    module = Mock()
    module.run_command = Mock(return_value=(0, 'Linux version 5.4.0', ''))
    
    from ansible.module_utils.facts.system.distribution import get_uname
    result = get_uname(module)
    
    module.run_command.assert_called_once_with(['uname', '-v'])
    assert result == 'Linux version 5.4.0'

def test_get_uname_failure(monkeypatch):
    module = Mock()
    module.run_command = Mock(return_value=(1, '', 'error'))
    
    from ansible.module_utils.facts.system.distribution import get_uname
    result = get_uname(module)
    
    module.run_command.assert_called_once_with(['uname', '-v'])
    assert result is None

def test_get_uname_with_string_flags(monkeypatch):
    module = Mock()
    module.run_command = Mock(return_value=(0, 'Linux version 5.4.0', ''))
    
    from ansible.module_utils.facts.system.distribution import get_uname
    result = get_uname(module, '-a')
    
    module.run_command.assert_called_once_with(['uname', '-a'])
    assert result == 'Linux version 5.4.0'

def test_get_uname_with_list_flags(monkeypatch):
    module = Mock()
    module.run_command = Mock(return_value=(0, 'Linux version 5.4.0', ''))
    
    from ansible.module_utils.facts.system.distribution import get_uname
    result = get_uname(module, ['-s', '-r'])
    
    module.run_command.assert_called_once_with(['uname', '-s', '-r'])
    assert result == 'Linux version 5.4.0'
