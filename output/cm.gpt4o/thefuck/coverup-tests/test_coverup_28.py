# file thefuck/conf.py:91-107
# lines [91, 93, 94, 95, 96, 97, 98, 100, 101, 103, 104, 105, 107]
# branches ['94->95', '94->96', '96->97', '96->98', '98->100', '98->101', '101->103', '101->104', '104->105', '104->107']

import os
import pytest
from unittest import mock

# Assuming the Settings class is imported from thefuck.conf
from thefuck.conf import Settings

@pytest.fixture
def mock_env():
    with mock.patch.dict(os.environ, {}, clear=True) as m:
        yield m

def test_val_from_env_rules(mock_env):
    settings = Settings()
    mock_env['TEST_RULES'] = 'rule1,rule2'
    with mock.patch.object(Settings, '_rules_from_env', return_value=['rule1', 'rule2']):
        assert settings._val_from_env('TEST_RULES', 'rules') == ['rule1', 'rule2']

def test_val_from_env_priority(mock_env):
    settings = Settings()
    mock_env['TEST_PRIORITY'] = 'cmd1=10,cmd2=20'
    with mock.patch.object(Settings, '_priority_from_env', return_value=[('cmd1', 10), ('cmd2', 20)]):
        assert settings._val_from_env('TEST_PRIORITY', 'priority') == {'cmd1': 10, 'cmd2': 20}

def test_val_from_env_int(mock_env):
    settings = Settings()
    mock_env['TEST_WAIT_COMMAND'] = '5'
    assert settings._val_from_env('TEST_WAIT_COMMAND', 'wait_command') == 5

def test_val_from_env_bool(mock_env):
    settings = Settings()
    mock_env['TEST_REQUIRE_CONFIRMATION'] = 'true'
    assert settings._val_from_env('TEST_REQUIRE_CONFIRMATION', 'require_confirmation') is True

def test_val_from_env_list(mock_env):
    settings = Settings()
    mock_env['TEST_SLOW_COMMANDS'] = 'cmd1:cmd2:cmd3'
    assert settings._val_from_env('TEST_SLOW_COMMANDS', 'slow_commands') == ['cmd1', 'cmd2', 'cmd3']

def test_val_from_env_default(mock_env):
    settings = Settings()
    mock_env['TEST_OTHER'] = 'some_value'
    assert settings._val_from_env('TEST_OTHER', 'other') == 'some_value'
