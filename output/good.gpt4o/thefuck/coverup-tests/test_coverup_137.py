# file thefuck/types.py:130-154
# lines [138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154]
# branches ['139->140', '139->142']

import pytest
import pathlib
from unittest import mock
from thefuck.types import Rule
from thefuck import logs
from thefuck.conf import settings

@pytest.fixture
def mock_settings(mocker):
    original_exclude_rules = settings.exclude_rules
    original_priority = settings.priority
    settings.exclude_rules = set()
    settings.priority = {}
    yield
    settings.exclude_rules = original_exclude_rules
    settings.priority = original_priority

@pytest.fixture
def mock_logs(mocker):
    mocker.patch('thefuck.logs.debug')
    mocker.patch('thefuck.logs.debug_time')
    mocker.patch('thefuck.logs.exception')

@pytest.fixture
def mock_load_source(mocker):
    return mocker.patch('thefuck.types.load_source')

def test_rule_from_path_excluded_rule(mock_settings, mock_logs):
    settings.exclude_rules.add('excluded_rule')
    path = pathlib.Path('excluded_rule.py')
    assert Rule.from_path(path) is None
    logs.debug.assert_called_once_with(u'Ignoring excluded rule: excluded_rule')

def test_rule_from_path_import_error(mock_settings, mock_logs, mock_load_source):
    path = pathlib.Path('error_rule.py')
    mock_load_source.side_effect = Exception('Import error')
    assert Rule.from_path(path) is None
    logs.exception.assert_called_once_with(u"Rule error_rule failed to load", mock.ANY)

def test_rule_from_path_success(mock_settings, mock_logs, mock_load_source):
    path = pathlib.Path('valid_rule.py')
    mock_rule_module = mock.Mock()
    mock_rule_module.priority = 1000
    mock_rule_module.match = mock.Mock()
    mock_rule_module.get_new_command = mock.Mock()
    mock_rule_module.enabled_by_default = True
    mock_rule_module.side_effect = None
    mock_rule_module.requires_output = True
    mock_load_source.return_value = mock_rule_module

    rule = Rule.from_path(path)
    assert rule.name == 'valid_rule'
    assert rule.match == mock_rule_module.match
    assert rule.get_new_command == mock_rule_module.get_new_command
    assert rule.enabled_by_default == True
    assert rule.side_effect == None
    assert rule.priority == 1000
    assert rule.requires_output == True
