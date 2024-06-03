# file lib/ansible/module_utils/facts/system/distribution.py:19-27
# lines [19, 20, 21, 22, 23, 24, 25, 26, 27]
# branches ['20->21', '20->22', '25->26', '25->27']

import pytest
from unittest.mock import Mock

# Assuming the function get_uname is part of a class or module, we need to import it.
# For this example, let's assume it's part of a module named 'distribution'.
from ansible.module_utils.facts.system.distribution import get_uname

def test_get_uname_with_string_flags(mocker):
    module = Mock()
    module.run_command = Mock(return_value=(0, 'Linux version 5.4.0', ''))
    
    result = get_uname(module, '-v')
    
    module.run_command.assert_called_once_with(['uname', '-v'])
    assert result == 'Linux version 5.4.0'

def test_get_uname_with_list_flags(mocker):
    module = Mock()
    module.run_command = Mock(return_value=(0, 'Linux version 5.4.0', ''))
    
    result = get_uname(module, ['-v'])
    
    module.run_command.assert_called_once_with(['uname', '-v'])
    assert result == 'Linux version 5.4.0'

def test_get_uname_failure(mocker):
    module = Mock()
    module.run_command = Mock(return_value=(1, '', 'error'))
    
    result = get_uname(module, '-v')
    
    module.run_command.assert_called_once_with(['uname', '-v'])
    assert result is None
