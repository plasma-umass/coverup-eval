# file: httpie/core.py:22-109
# asked: {"lines": [22, 32, 33, 34, 35, 37, 39, 40, 42, 43, 45, 46, 47, 48, 50, 52, 53, 54, 55, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 69, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 94, 96, 97, 98, 99, 100, 101, 102, 104, 105, 106, 107, 109], "branches": [[39, 40], [39, 42], [45, 46], [45, 50], [47, 48], [47, 50], [59, 60], [59, 61], [63, 64], [63, 109], [65, 66], [65, 67], [76, 77], [76, 78], [80, 81], [80, 109], [82, 83], [82, 84], [97, 98], [97, 104], [99, 100], [99, 104], [105, 106], [105, 107]]}
# gained: {"lines": [22, 32, 33, 34, 35, 37, 39, 42, 43, 45, 46, 47, 48, 50, 52, 53, 54, 55, 57, 58, 59, 61, 62, 63, 64, 65, 67, 69, 70, 71, 72, 74, 79, 85, 86, 87, 88, 89, 90, 91, 92, 94, 96, 97, 104, 105, 107, 109], "branches": [[39, 42], [45, 46], [45, 50], [47, 48], [59, 61], [63, 64], [65, 67], [97, 104], [105, 107]]}

import pytest
from unittest.mock import patch, MagicMock
from httpie.core import main
from httpie.context import Environment
from httpie.status import ExitStatus
import requests
from httpie.cli.definition import parser

@pytest.fixture
def mock_env():
    env = Environment()
    env.program_name = 'http'
    env._config = MagicMock()
    env._config.default_options = []
    env.stdin_encoding = 'utf-8'
    env.stderr = MagicMock()
    env.stdout = MagicMock()
    env.stdout_isatty = False
    return env

def test_main_success(mock_env):
    with patch('httpie.core.decode_raw_args', return_value=['https://example.com']), \
         patch('httpie.core.plugin_manager.load_installed_plugins'), \
         patch.object(parser, 'parse_args', return_value=MagicMock()), \
         patch('httpie.core.program', return_value=ExitStatus.SUCCESS):
        assert main(['http', 'https://example.com'], env=mock_env) == ExitStatus.SUCCESS

def test_main_debug(mock_env):
    with patch('httpie.core.decode_raw_args', return_value=['--debug']), \
         patch('httpie.core.plugin_manager.load_installed_plugins'), \
         patch('httpie.core.print_debug_info') as mock_print_debug_info:
        assert main(['http', '--debug'], env=mock_env) == ExitStatus.SUCCESS
        mock_print_debug_info.assert_called_once_with(mock_env)

def test_main_keyboard_interrupt(mock_env):
    with patch('httpie.core.decode_raw_args', return_value=['https://example.com']), \
         patch('httpie.core.plugin_manager.load_installed_plugins'), \
         patch.object(parser, 'parse_args', side_effect=KeyboardInterrupt):
        assert main(['http', 'https://example.com'], env=mock_env) == ExitStatus.ERROR_CTRL_C

def test_main_system_exit(mock_env):
    with patch('httpie.core.decode_raw_args', return_value=['https://example.com']), \
         patch('httpie.core.plugin_manager.load_installed_plugins'), \
         patch.object(parser, 'parse_args', side_effect=SystemExit(1)):
        assert main(['http', 'https://example.com'], env=mock_env) == ExitStatus.ERROR

def test_main_requests_timeout(mock_env):
    with patch('httpie.core.decode_raw_args', return_value=['https://example.com']), \
         patch('httpie.core.plugin_manager.load_installed_plugins'), \
         patch.object(parser, 'parse_args', return_value=MagicMock()), \
         patch('httpie.core.program', side_effect=requests.Timeout):
        assert main(['http', 'https://example.com'], env=mock_env) == ExitStatus.ERROR_TIMEOUT

def test_main_requests_too_many_redirects(mock_env):
    with patch('httpie.core.decode_raw_args', return_value=['https://example.com']), \
         patch('httpie.core.plugin_manager.load_installed_plugins'), \
         patch.object(parser, 'parse_args', return_value=MagicMock()), \
         patch('httpie.core.program', side_effect=requests.TooManyRedirects):
        assert main(['http', 'https://example.com'], env=mock_env) == ExitStatus.ERROR_TOO_MANY_REDIRECTS

def test_main_generic_exception(mock_env):
    with patch('httpie.core.decode_raw_args', return_value=['https://example.com']), \
         patch('httpie.core.plugin_manager.load_installed_plugins'), \
         patch.object(parser, 'parse_args', return_value=MagicMock()), \
         patch('httpie.core.program', side_effect=Exception('Test Exception')):
        assert main(['http', 'https://example.com'], env=mock_env) == ExitStatus.ERROR
