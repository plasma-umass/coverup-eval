# file: tornado/options.py:710-715
# asked: {"lines": [715], "branches": []}
# gained: {"lines": [715], "branches": []}

import pytest
from unittest import mock
from tornado.options import parse_config_file, options

def test_parse_config_file(monkeypatch):
    mock_parse_config_file = mock.Mock()
    monkeypatch.setattr(options.__class__, 'parse_config_file', mock_parse_config_file)
    
    test_path = "test_config.cfg"
    parse_config_file(test_path, final=False)
    
    mock_parse_config_file.assert_called_once_with(test_path, final=False)
