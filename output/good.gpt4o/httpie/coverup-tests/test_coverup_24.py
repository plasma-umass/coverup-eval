# file httpie/core.py:221-231
# lines [221, 222, 223, 224, 225, 226, 227, 229, 230, 231]
# branches []

import pytest
from unittest.mock import Mock, patch
from httpie.core import print_debug_info
from httpie.context import Environment

def test_print_debug_info(mocker):
    mock_stderr = Mock()
    env = Environment(stderr=mock_stderr)

    with patch('httpie.core.httpie_version', '1.0.0'), \
         patch('httpie.core.requests_version', '2.25.1'), \
         patch('httpie.core.pygments_version', '2.7.4'), \
         patch('httpie.core.sys.version', '3.9.1'), \
         patch('httpie.core.sys.executable', '/usr/bin/python3'), \
         patch('httpie.core.platform.system', return_value='Linux'), \
         patch('httpie.core.platform.release', return_value='5.4.0-42-generic'):
        
        print_debug_info(env)

    expected_output = (
        'HTTPie 1.0.0\n'
        'Requests 2.25.1\n'
        'Pygments 2.7.4\n'
        'Python 3.9.1\n/usr/bin/python3\n'
        'Linux 5.4.0-42-generic\n\n'
        f'{repr(env)}\n'
    )
    
    mock_stderr.writelines.assert_called_once_with([
        'HTTPie 1.0.0\n',
        'Requests 2.25.1\n',
        'Pygments 2.7.4\n',
        'Python 3.9.1\n/usr/bin/python3\n',
        'Linux 5.4.0-42-generic'
    ])
    mock_stderr.write.assert_any_call('\n\n')
    mock_stderr.write.assert_any_call(repr(env))
    mock_stderr.write.assert_any_call('\n')
