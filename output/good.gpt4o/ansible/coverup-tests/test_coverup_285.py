# file lib/ansible/module_utils/facts/system/cmdline.py:33-45
# lines [33, 34, 35, 36, 37, 38, 39, 41, 42, 43, 45]
# branches ['36->37', '36->45', '38->39', '38->41']

import pytest
from ansible.module_utils.facts.system.cmdline import CmdLineFactCollector

def test_parse_proc_cmdline(mocker):
    collector = CmdLineFactCollector()

    # Mock data to cover different branches
    data = 'param1=value1 param2="value with spaces" param3 param4="unterminated'

    # Mock shlex.split to raise ValueError for testing exception handling
    mocker.patch('shlex.split', side_effect=ValueError)

    # Test the function
    result = collector._parse_proc_cmdline(data)

    # Assertions to verify postconditions
    assert result == {}

    # Reset the mock to test normal behavior
    mocker.patch('shlex.split', side_effect=None, return_value=['param1=value1', 'param2=value with spaces', 'param3', 'param4=unterminated'])

    # Test the function again
    result = collector._parse_proc_cmdline(data)

    # Assertions to verify postconditions
    assert result == {
        'param1': 'value1',
        'param2': 'value with spaces',
        'param3': True,
        'param4': 'unterminated'
    }
