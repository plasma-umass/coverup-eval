# file: lib/ansible/module_utils/facts/other/ohai.py:26-72
# asked: {"lines": [26, 27, 28, 29, 31, 32, 33, 34, 35, 37, 38, 39, 41, 42, 43, 45, 46, 47, 48, 50, 51, 52, 54, 56, 57, 58, 59, 61, 63, 64, 66, 67, 68, 70, 72], "branches": [[47, 48], [47, 50], [51, 52], [51, 54], [58, 59], [58, 61], [63, 64], [63, 66]]}
# gained: {"lines": [26, 27, 28, 29, 31, 32, 33, 34, 35, 37, 38, 39, 41, 42, 43, 45, 46, 47, 48, 50, 51, 52, 54, 56, 57, 58, 59, 61, 63, 64, 66, 67, 68, 70, 72], "branches": [[47, 48], [47, 50], [51, 52], [51, 54], [58, 59], [58, 61], [63, 64], [63, 66]]}

import pytest
import json
from unittest.mock import Mock, patch
from ansible.module_utils.facts.other.ohai import OhaiFactCollector

@pytest.fixture
def mock_module():
    return Mock()

def test_init():
    collector = OhaiFactCollector()
    assert collector.namespace.namespace_name == 'ohai'
    assert collector.namespace.prefix == 'ohai_'

def test_find_ohai(mock_module):
    mock_module.get_bin_path.return_value = '/usr/bin/ohai'
    collector = OhaiFactCollector()
    ohai_path = collector.find_ohai(mock_module)
    assert ohai_path == '/usr/bin/ohai'
    mock_module.get_bin_path.assert_called_once_with('ohai')

def test_run_ohai(mock_module):
    mock_module.run_command.return_value = (0, 'output', 'error')
    collector = OhaiFactCollector()
    rc, out, err = collector.run_ohai(mock_module, '/usr/bin/ohai')
    assert rc == 0
    assert out == 'output'
    assert err == 'error'
    mock_module.run_command.assert_called_once_with('/usr/bin/ohai')

def test_get_ohai_output_no_path(mock_module):
    mock_module.get_bin_path.return_value = None
    collector = OhaiFactCollector()
    output = collector.get_ohai_output(mock_module)
    assert output is None
    mock_module.get_bin_path.assert_called_once_with('ohai')

def test_get_ohai_output_command_fail(mock_module):
    mock_module.get_bin_path.return_value = '/usr/bin/ohai'
    mock_module.run_command.return_value = (1, '', 'error')
    collector = OhaiFactCollector()
    output = collector.get_ohai_output(mock_module)
    assert output is None
    mock_module.get_bin_path.assert_called_once_with('ohai')
    mock_module.run_command.assert_called_once_with('/usr/bin/ohai')

def test_get_ohai_output_success(mock_module):
    mock_module.get_bin_path.return_value = '/usr/bin/ohai'
    mock_module.run_command.return_value = (0, 'output', '')
    collector = OhaiFactCollector()
    output = collector.get_ohai_output(mock_module)
    assert output == 'output'
    mock_module.get_bin_path.assert_called_once_with('ohai')
    mock_module.run_command.assert_called_once_with('/usr/bin/ohai')

def test_collect_no_module():
    collector = OhaiFactCollector()
    facts = collector.collect()
    assert facts == {}

def test_collect_no_ohai_output(mock_module):
    mock_module.get_bin_path.return_value = None
    collector = OhaiFactCollector()
    facts = collector.collect(module=mock_module)
    assert facts == {}
    mock_module.get_bin_path.assert_called_once_with('ohai')

def test_collect_with_ohai_output(mock_module):
    mock_module.get_bin_path.return_value = '/usr/bin/ohai'
    mock_module.run_command.return_value = (0, '{"key": "value"}', '')
    collector = OhaiFactCollector()
    facts = collector.collect(module=mock_module)
    assert facts == {"key": "value"}
    mock_module.get_bin_path.assert_called_once_with('ohai')
    mock_module.run_command.assert_called_once_with('/usr/bin/ohai')

def test_collect_with_ohai_output_invalid_json(mock_module):
    mock_module.get_bin_path.return_value = '/usr/bin/ohai'
    mock_module.run_command.return_value = (0, 'invalid json', '')
    collector = OhaiFactCollector()
    facts = collector.collect(module=mock_module)
    assert facts == {}
    mock_module.get_bin_path.assert_called_once_with('ohai')
    mock_module.run_command.assert_called_once_with('/usr/bin/ohai')
