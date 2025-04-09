# file: httpie/core.py:22-109
# asked: {"lines": [22, 32, 33, 34, 35, 37, 39, 40, 42, 43, 45, 46, 47, 48, 50, 52, 53, 54, 55, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 69, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 94, 96, 97, 98, 99, 100, 101, 102, 104, 105, 106, 107, 109], "branches": [[39, 40], [39, 42], [45, 46], [45, 50], [47, 48], [47, 50], [59, 60], [59, 61], [63, 64], [63, 109], [65, 66], [65, 67], [76, 77], [76, 78], [80, 81], [80, 109], [82, 83], [82, 84], [97, 98], [97, 104], [99, 100], [99, 104], [105, 106], [105, 107]]}
# gained: {"lines": [22, 32, 33, 34, 35, 37, 39, 42, 43, 45, 46, 47, 48, 50, 52, 53, 54, 55, 57, 58, 59, 61, 62, 63, 64, 65, 67, 69, 70, 71, 72, 74, 79, 85, 86, 87, 88, 89, 90, 91, 92, 94, 96, 97, 104, 105, 107, 109], "branches": [[39, 42], [45, 46], [45, 50], [47, 48], [59, 61], [63, 64], [65, 67], [97, 104], [105, 107]]}

import pytest
from unittest.mock import Mock, patch
from httpie.core import main, Environment, ExitStatus
import sys
import os
import requests

@pytest.fixture
def mock_env():
    env = Mock(spec=Environment)
    env.program_name = 'http'
    env.stdin_encoding = 'utf-8'
    env.config.default_options = []
    env.stderr = Mock()
    return env

def test_main_success(mock_env, monkeypatch):
    args = ['http', 'example.com']
    monkeypatch.setattr(sys, 'argv', args)
    monkeypatch.setattr('httpie.core.decode_raw_args', lambda x, y: x)
    monkeypatch.setattr('httpie.core.plugin_manager.load_installed_plugins', lambda: None)
    monkeypatch.setattr('httpie.cli.definition.parser.parse_args', lambda args, env: args)
    monkeypatch.setattr('httpie.core.program', lambda args, env: ExitStatus.SUCCESS)
    
    exit_status = main(args, env=mock_env)
    assert exit_status == ExitStatus.SUCCESS

def test_main_debug(mock_env, monkeypatch):
    args = ['http', '--debug']
    monkeypatch.setattr(sys, 'argv', args)
    monkeypatch.setattr('httpie.core.decode_raw_args', lambda x, y: x)
    monkeypatch.setattr('httpie.core.plugin_manager.load_installed_plugins', lambda: None)
    monkeypatch.setattr('httpie.core.print_debug_info', lambda env: None)
    
    exit_status = main(args, env=mock_env)
    assert exit_status == ExitStatus.SUCCESS

def test_main_keyboard_interrupt(mock_env, monkeypatch):
    args = ['http', 'example.com']
    monkeypatch.setattr(sys, 'argv', args)
    monkeypatch.setattr('httpie.core.decode_raw_args', lambda x, y: x)
    monkeypatch.setattr('httpie.core.plugin_manager.load_installed_plugins', lambda: None)
    monkeypatch.setattr('httpie.cli.definition.parser.parse_args', Mock(side_effect=KeyboardInterrupt))
    
    exit_status = main(args, env=mock_env)
    assert exit_status == ExitStatus.ERROR_CTRL_C

def test_main_system_exit(mock_env, monkeypatch):
    args = ['http', 'example.com']
    monkeypatch.setattr(sys, 'argv', args)
    monkeypatch.setattr('httpie.core.decode_raw_args', lambda x, y: x)
    monkeypatch.setattr('httpie.core.plugin_manager.load_installed_plugins', lambda: None)
    monkeypatch.setattr('httpie.cli.definition.parser.parse_args', Mock(side_effect=SystemExit(1)))
    
    exit_status = main(args, env=mock_env)
    assert exit_status == ExitStatus.ERROR

def test_main_requests_timeout(mock_env, monkeypatch):
    args = ['http', 'example.com']
    monkeypatch.setattr(sys, 'argv', args)
    monkeypatch.setattr('httpie.core.decode_raw_args', lambda x, y: x)
    monkeypatch.setattr('httpie.core.plugin_manager.load_installed_plugins', lambda: None)
    monkeypatch.setattr('httpie.cli.definition.parser.parse_args', lambda args, env: Mock(timeout=30))
    monkeypatch.setattr('httpie.core.program', Mock(side_effect=requests.Timeout))
    
    exit_status = main(args, env=mock_env)
    assert exit_status == ExitStatus.ERROR_TIMEOUT

def test_main_requests_too_many_redirects(mock_env, monkeypatch):
    args = ['http', 'example.com']
    monkeypatch.setattr(sys, 'argv', args)
    monkeypatch.setattr('httpie.core.decode_raw_args', lambda x, y: x)
    monkeypatch.setattr('httpie.core.plugin_manager.load_installed_plugins', lambda: None)
    monkeypatch.setattr('httpie.cli.definition.parser.parse_args', lambda args, env: Mock(max_redirects=10))
    monkeypatch.setattr('httpie.core.program', Mock(side_effect=requests.TooManyRedirects))
    
    exit_status = main(args, env=mock_env)
    assert exit_status == ExitStatus.ERROR_TOO_MANY_REDIRECTS

def test_main_generic_exception(mock_env, monkeypatch):
    args = ['http', 'example.com']
    monkeypatch.setattr(sys, 'argv', args)
    monkeypatch.setattr('httpie.core.decode_raw_args', lambda x, y: x)
    monkeypatch.setattr('httpie.core.plugin_manager.load_installed_plugins', lambda: None)
    monkeypatch.setattr('httpie.cli.definition.parser.parse_args', lambda args, env: args)
    monkeypatch.setattr('httpie.core.program', Mock(side_effect=Exception('Test Exception')))
    
    exit_status = main(args, env=mock_env)
    assert exit_status == ExitStatus.ERROR
