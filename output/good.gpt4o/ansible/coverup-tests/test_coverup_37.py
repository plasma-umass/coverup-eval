# file lib/ansible/module_utils/facts/other/ohai.py:26-72
# lines [26, 27, 28, 29, 31, 32, 33, 34, 35, 37, 38, 39, 41, 42, 43, 45, 46, 47, 48, 50, 51, 52, 54, 56, 57, 58, 59, 61, 63, 64, 66, 67, 68, 70, 72]
# branches ['47->48', '47->50', '51->52', '51->54', '58->59', '58->61', '63->64', '63->66']

import pytest
import json
from ansible.module_utils.facts.other.ohai import OhaiFactCollector
from unittest.mock import Mock

@pytest.fixture
def mock_module():
    return Mock()

@pytest.fixture
def ohai_collector():
    return OhaiFactCollector()

def test_find_ohai(mock_module, ohai_collector):
    mock_module.get_bin_path.return_value = '/usr/bin/ohai'
    ohai_path = ohai_collector.find_ohai(mock_module)
    assert ohai_path == '/usr/bin/ohai'
    mock_module.get_bin_path.assert_called_once_with('ohai')

def test_run_ohai(mock_module, ohai_collector):
    mock_module.run_command.return_value = (0, '{"key": "value"}', '')
    rc, out, err = ohai_collector.run_ohai(mock_module, '/usr/bin/ohai')
    assert rc == 0
    assert out == '{"key": "value"}'
    assert err == ''
    mock_module.run_command.assert_called_once_with('/usr/bin/ohai')

def test_get_ohai_output_success(mock_module, ohai_collector):
    mock_module.get_bin_path.return_value = '/usr/bin/ohai'
    mock_module.run_command.return_value = (0, '{"key": "value"}', '')
    output = ohai_collector.get_ohai_output(mock_module)
    assert output == '{"key": "value"}'
    mock_module.get_bin_path.assert_called_once_with('ohai')
    mock_module.run_command.assert_called_once_with('/usr/bin/ohai')

def test_get_ohai_output_no_ohai(mock_module, ohai_collector):
    mock_module.get_bin_path.return_value = None
    output = ohai_collector.get_ohai_output(mock_module)
    assert output is None
    mock_module.get_bin_path.assert_called_once_with('ohai')

def test_get_ohai_output_failure(mock_module, ohai_collector):
    mock_module.get_bin_path.return_value = '/usr/bin/ohai'
    mock_module.run_command.return_value = (1, '', 'error')
    output = ohai_collector.get_ohai_output(mock_module)
    assert output is None
    mock_module.get_bin_path.assert_called_once_with('ohai')
    mock_module.run_command.assert_called_once_with('/usr/bin/ohai')

def test_collect_no_module(ohai_collector):
    facts = ohai_collector.collect(module=None)
    assert facts == {}

def test_collect_with_module_success(mock_module, ohai_collector):
    mock_module.get_bin_path.return_value = '/usr/bin/ohai'
    mock_module.run_command.return_value = (0, '{"key": "value"}', '')
    facts = ohai_collector.collect(module=mock_module)
    assert facts == {"key": "value"}
    mock_module.get_bin_path.assert_called_once_with('ohai')
    mock_module.run_command.assert_called_once_with('/usr/bin/ohai')

def test_collect_with_module_failure(mock_module, ohai_collector):
    mock_module.get_bin_path.return_value = '/usr/bin/ohai'
    mock_module.run_command.return_value = (1, '', 'error')
    facts = ohai_collector.collect(module=mock_module)
    assert facts == {}
    mock_module.get_bin_path.assert_called_once_with('ohai')
    mock_module.run_command.assert_called_once_with('/usr/bin/ohai')

def test_collect_with_invalid_json(mock_module, ohai_collector):
    mock_module.get_bin_path.return_value = '/usr/bin/ohai'
    mock_module.run_command.return_value = (0, 'invalid json', '')
    facts = ohai_collector.collect(module=mock_module)
    assert facts == {}
    mock_module.get_bin_path.assert_called_once_with('ohai')
    mock_module.run_command.assert_called_once_with('/usr/bin/ohai')
