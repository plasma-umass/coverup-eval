# file thefuck/conf.py:91-107
# lines [91, 93, 94, 95, 96, 97, 98, 100, 101, 103, 104, 105, 107]
# branches ['94->95', '94->96', '96->97', '96->98', '98->100', '98->101', '101->103', '101->104', '104->105', '104->107']

import os
import pytest
from thefuck.conf import Settings

@pytest.fixture
def settings():
    return Settings()

@pytest.fixture
def env_vars(mocker):
    mocker.patch.dict(os.environ, {
        'THEFUCK_RULES': 'rule1:rule2',
        'THEFUCK_EXCLUDE_RULES': 'exclude_rule1:exclude_rule2',
        'THEFUCK_PRIORITY': 'sudo=10:apt_get=5',
        'THEFUCK_WAIT_COMMAND': '3',
        'THEFUCK_HISTORY_LIMIT': '1000',
        'THEFUCK_WAIT_SLOW_COMMAND': '10',
        'THEFUCK_NUM_CLOSE_MATCHES': '5',
        'THEFUCK_REQUIRE_CONFIRMATION': 'true',
        'THEFUCK_NO_COLORS': 'false',
        'THEFUCK_DEBUG': 'true',
        'THEFUCK_ALTER_HISTORY': 'false',
        'THEFUCK_INSTANT_MODE': 'true',
        'THEFUCK_SLOW_COMMANDS': 'lein:react-native:./gradlew',
        'THEFUCK_EXCLUDED_SEARCH_PATH_PREFIXES': '/usr/local/bin:/bin'
    })

def test_val_from_env(settings, env_vars):
    assert settings._val_from_env('THEFUCK_RULES', 'rules') == ['rule1', 'rule2']
    assert settings._val_from_env('THEFUCK_EXCLUDE_RULES', 'exclude_rules') == ['exclude_rule1', 'exclude_rule2']
    assert settings._val_from_env('THEFUCK_PRIORITY', 'priority') == {'sudo': 10, 'apt_get': 5}
    assert settings._val_from_env('THEFUCK_WAIT_COMMAND', 'wait_command') == 3
    assert settings._val_from_env('THEFUCK_HISTORY_LIMIT', 'history_limit') == 1000
    assert settings._val_from_env('THEFUCK_WAIT_SLOW_COMMAND', 'wait_slow_command') == 10
    assert settings._val_from_env('THEFUCK_NUM_CLOSE_MATCHES', 'num_close_matches') == 5
    assert settings._val_from_env('THEFUCK_REQUIRE_CONFIRMATION', 'require_confirmation') is True
    assert settings._val_from_env('THEFUCK_NO_COLORS', 'no_colors') is False
    assert settings._val_from_env('THEFUCK_DEBUG', 'debug') is True
    assert settings._val_from_env('THEFUCK_ALTER_HISTORY', 'alter_history') is False
    assert settings._val_from_env('THEFUCK_INSTANT_MODE', 'instant_mode') is True
    assert settings._val_from_env('THEFUCK_SLOW_COMMANDS', 'slow_commands') == ['lein', 'react-native', './gradlew']
    assert settings._val_from_env('THEFUCK_EXCLUDED_SEARCH_PATH_PREFIXES', 'excluded_search_path_prefixes') == ['/usr/local/bin', '/bin']
