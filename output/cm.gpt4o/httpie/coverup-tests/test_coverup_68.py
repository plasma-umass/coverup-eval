# file httpie/core.py:22-109
# lines [22, 32, 33, 34, 35, 37, 39, 40, 42, 43, 45, 46, 47, 48, 50, 52, 53, 54, 55, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 69, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 94, 96, 97, 98, 99, 100, 101, 102, 104, 105, 106, 107, 109]
# branches ['39->40', '39->42', '45->46', '45->50', '47->48', '47->50', '59->60', '59->61', '63->64', '63->109', '65->66', '65->67', '76->77', '76->78', '80->81', '80->109', '82->83', '82->84', '97->98', '97->104', '99->100', '99->104', '105->106', '105->107']

import pytest
from unittest import mock
from httpie.core import main, ExitStatus
from httpie.context import Environment
import requests

def test_main_with_debug(mocker):
    mock_env = mocker.Mock(spec=Environment)
    mock_env.program_name = 'http'
    mock_env.stdin_encoding = 'utf-8'
    mock_env.config.default_options = []
    mock_env.stderr.write = mocker.Mock()
    mock_env.log_error = mocker.Mock()

    mocker.patch('httpie.core.decode_raw_args', return_value=['--debug'])
    mocker.patch('httpie.core.plugin_manager.load_installed_plugins')
    mocker.patch('httpie.cli.definition.parser.parse_args', side_effect=SystemExit(0))
    mocker.patch('httpie.core.print_debug_info')

    exit_status = main(['http', '--debug'], env=mock_env)
    assert exit_status == ExitStatus.SUCCESS
    mock_env.stderr.write.assert_not_called()
    mock_env.log_error.assert_not_called()

def test_main_with_keyboard_interrupt(mocker):
    mock_env = mocker.Mock(spec=Environment)
    mock_env.program_name = 'http'
    mock_env.stdin_encoding = 'utf-8'
    mock_env.config.default_options = []
    mock_env.stderr.write = mocker.Mock()
    mock_env.log_error = mocker.Mock()

    mocker.patch('httpie.core.decode_raw_args', return_value=['--some-arg'])
    mocker.patch('httpie.core.plugin_manager.load_installed_plugins')
    mocker.patch('httpie.cli.definition.parser.parse_args', side_effect=KeyboardInterrupt)

    exit_status = main(['http', '--some-arg'], env=mock_env)
    assert exit_status == ExitStatus.ERROR_CTRL_C
    mock_env.stderr.write.assert_called_once_with('\n')
    mock_env.log_error.assert_not_called()

def test_main_with_system_exit_error(mocker):
    mock_env = mocker.Mock(spec=Environment)
    mock_env.program_name = 'http'
    mock_env.stdin_encoding = 'utf-8'
    mock_env.config.default_options = []
    mock_env.stderr.write = mocker.Mock()
    mock_env.log_error = mocker.Mock()

    mocker.patch('httpie.core.decode_raw_args', return_value=['--some-arg'])
    mocker.patch('httpie.core.plugin_manager.load_installed_plugins')
    mocker.patch('httpie.cli.definition.parser.parse_args', side_effect=SystemExit(1))

    exit_status = main(['http', '--some-arg'], env=mock_env)
    assert exit_status == ExitStatus.ERROR
    mock_env.stderr.write.assert_called_once_with('\n')
    mock_env.log_error.assert_not_called()

def test_main_with_requests_timeout(mocker):
    mock_env = mocker.Mock(spec=Environment)
    mock_env.program_name = 'http'
    mock_env.stdin_encoding = 'utf-8'
    mock_env.config.default_options = []
    mock_env.stderr.write = mocker.Mock()
    mock_env.log_error = mocker.Mock()

    mocker.patch('httpie.core.decode_raw_args', return_value=['--some-arg'])
    mocker.patch('httpie.core.plugin_manager.load_installed_plugins')
    mocker.patch('httpie.cli.definition.parser.parse_args', return_value=mocker.Mock())
    mocker.patch('httpie.core.program', side_effect=requests.Timeout)
    mock_parsed_args = mocker.Mock()
    mock_parsed_args.timeout = 30
    mocker.patch('httpie.cli.definition.parser.parse_args', return_value=mock_parsed_args)

    exit_status = main(['http', '--some-arg'], env=mock_env)
    assert exit_status == ExitStatus.ERROR_TIMEOUT
    mock_env.log_error.assert_called_once_with('Request timed out (30s).')

def test_main_with_too_many_redirects(mocker):
    mock_env = mocker.Mock(spec=Environment)
    mock_env.program_name = 'http'
    mock_env.stdin_encoding = 'utf-8'
    mock_env.config.default_options = []
    mock_env.stderr.write = mocker.Mock()
    mock_env.log_error = mocker.Mock()

    mocker.patch('httpie.core.decode_raw_args', return_value=['--some-arg'])
    mocker.patch('httpie.core.plugin_manager.load_installed_plugins')
    mock_parsed_args = mocker.Mock()
    mock_parsed_args.max_redirects = 10
    mocker.patch('httpie.cli.definition.parser.parse_args', return_value=mock_parsed_args)
    mocker.patch('httpie.core.program', side_effect=requests.TooManyRedirects)

    exit_status = main(['http', '--some-arg'], env=mock_env)
    assert exit_status == ExitStatus.ERROR_TOO_MANY_REDIRECTS
    mock_env.log_error.assert_called_once_with('Too many redirects (--max-redirects=10).')

def test_main_with_generic_exception(mocker):
    mock_env = mocker.Mock(spec=Environment)
    mock_env.program_name = 'http'
    mock_env.stdin_encoding = 'utf-8'
    mock_env.config.default_options = []
    mock_env.stderr.write = mocker.Mock()
    mock_env.log_error = mocker.Mock()

    mocker.patch('httpie.core.decode_raw_args', return_value=['--some-arg'])
    mocker.patch('httpie.core.plugin_manager.load_installed_plugins')
    mocker.patch('httpie.cli.definition.parser.parse_args', return_value=mocker.Mock())
    mocker.patch('httpie.core.program', side_effect=Exception('Test exception'))

    exit_status = main(['http', '--some-arg'], env=mock_env)
    assert exit_status == ExitStatus.ERROR
    mock_env.log_error.assert_called_once_with('Exception: Test exception')
