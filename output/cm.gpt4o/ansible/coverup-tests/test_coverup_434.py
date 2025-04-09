# file lib/ansible/config/manager.py:187-195
# lines [187, 189, 190, 191, 192, 193, 194, 195]
# branches ['190->191', '190->195']

import pytest
from unittest import mock
from ansible.config.manager import get_ini_config_value

@pytest.fixture
def mock_parser():
    return mock.Mock()

def test_get_ini_config_value_success(mock_parser):
    mock_parser.get.return_value = 'test_value'
    entry = {'section': 'defaults', 'key': 'test_key'}
    result = get_ini_config_value(mock_parser, entry)
    assert result == 'test_value'
    mock_parser.get.assert_called_once_with('defaults', 'test_key', raw=True)

def test_get_ini_config_value_no_parser():
    entry = {'section': 'defaults', 'key': 'test_key'}
    result = get_ini_config_value(None, entry)
    assert result is None

def test_get_ini_config_value_exception(mock_parser):
    mock_parser.get.side_effect = Exception("Test Exception")
    entry = {'section': 'defaults', 'key': 'test_key'}
    result = get_ini_config_value(mock_parser, entry)
    assert result is None
    mock_parser.get.assert_called_once_with('defaults', 'test_key', raw=True)
