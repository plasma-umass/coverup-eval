# file: httpie/core.py:221-231
# asked: {"lines": [221, 222, 223, 224, 225, 226, 227, 229, 230, 231], "branches": []}
# gained: {"lines": [221, 222, 223, 224, 225, 226, 227, 229, 230, 231], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from httpie.core import print_debug_info
from httpie.context import Environment

@pytest.fixture
def mock_env():
    env = MagicMock(spec=Environment)
    env.stderr = MagicMock()
    return env

def test_print_debug_info(mock_env):
    with patch('httpie.core.httpie_version', '1.0.0'), \
         patch('httpie.core.requests_version', '2.25.1'), \
         patch('httpie.core.pygments_version', '2.7.4'), \
         patch('httpie.core.sys.version', '3.9.1'), \
         patch('httpie.core.sys.executable', '/usr/bin/python3'), \
         patch('httpie.core.platform.system', return_value='Linux'), \
         patch('httpie.core.platform.release', return_value='5.4.0-66-generic'):
        
        print_debug_info(mock_env)
        
        mock_env.stderr.writelines.assert_called_once_with([
            'HTTPie 1.0.0\n',
            'Requests 2.25.1\n',
            'Pygments 2.7.4\n',
            'Python 3.9.1\n/usr/bin/python3\n',
            'Linux 5.4.0-66-generic',
        ])
        assert mock_env.stderr.write.call_count == 3
        mock_env.stderr.write.assert_any_call('\n\n')
        mock_env.stderr.write.assert_any_call(repr(mock_env))
        mock_env.stderr.write.assert_any_call('\n')
