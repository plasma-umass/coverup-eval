# file: lib/ansible/cli/arguments/option_helpers.py:301-306
# asked: {"lines": [301, 303, 304, 305, 306], "branches": []}
# gained: {"lines": [301, 303, 304, 305, 306], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from ansible.cli.arguments.option_helpers import add_module_options
from ansible import constants as C
import argparse

@pytest.fixture
def mock_parser():
    return MagicMock(spec=argparse.ArgumentParser)

@pytest.fixture
def mock_config(monkeypatch):
    mock_get_configuration_definition = MagicMock()
    mock_get_configuration_definition.return_value.get.return_value = '/default/module/path'
    monkeypatch.setattr(C.config, 'get_configuration_definition', mock_get_configuration_definition)
    return mock_get_configuration_definition

def mock_unfrack_path(pathsep=False):
    def inner(value):
        if pathsep:
            return value.split(':')
        return value
    return inner

@patch('ansible.cli.arguments.option_helpers.unfrack_path', side_effect=mock_unfrack_path)
def test_add_module_options(mock_unfrack_path, mock_parser, mock_config):
    add_module_options(mock_parser)
    
    mock_parser.add_argument.assert_called_once()
    args, kwargs = mock_parser.add_argument.call_args
    assert args == ('-M', '--module-path')
    assert kwargs['dest'] == 'module_path'
    assert kwargs['default'] is None
    assert kwargs['help'] == "prepend colon-separated path(s) to module library (default=/default/module/path)"
    assert callable(kwargs['type'])
    assert kwargs['action'].__name__ == 'PrependListAction'
