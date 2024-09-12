# file: lib/ansible/module_utils/facts/other/ohai.py:26-72
# asked: {"lines": [26, 27, 28, 29, 31, 32, 33, 34, 35, 37, 38, 39, 41, 42, 43, 45, 46, 47, 48, 50, 51, 52, 54, 56, 57, 58, 59, 61, 63, 64, 66, 67, 68, 70, 72], "branches": [[47, 48], [47, 50], [51, 52], [51, 54], [58, 59], [58, 61], [63, 64], [63, 66]]}
# gained: {"lines": [26, 27, 28, 29, 31, 32, 33, 34, 35, 37, 38, 39, 41, 42, 43, 45, 46, 47, 48, 50, 51, 52, 54, 56, 57, 58, 59, 61, 63, 64, 66, 67, 68, 70, 72], "branches": [[47, 48], [47, 50], [51, 52], [51, 54], [58, 59], [58, 61], [63, 64], [63, 66]]}

import pytest
import json
from ansible.module_utils.facts.other.ohai import OhaiFactCollector
from ansible.module_utils.facts.namespace import PrefixFactNamespace
from ansible.module_utils.facts.collector import BaseFactCollector

class MockModule:
    def __init__(self, bin_path=None, run_command_result=None):
        self.bin_path = bin_path
        self.run_command_result = run_command_result

    def get_bin_path(self, name):
        return self.bin_path

    def run_command(self, command):
        return self.run_command_result

@pytest.fixture
def mock_module():
    return MockModule()

def test_find_ohai(mock_module):
    collector = OhaiFactCollector()
    mock_module.bin_path = '/usr/bin/ohai'
    assert collector.find_ohai(mock_module) == '/usr/bin/ohai'

def test_run_ohai(mock_module):
    collector = OhaiFactCollector()
    mock_module.run_command_result = (0, 'output', '')
    rc, out, err = collector.run_ohai(mock_module, '/usr/bin/ohai')
    assert rc == 0
    assert out == 'output'
    assert err == ''

def test_get_ohai_output_success(mock_module):
    collector = OhaiFactCollector()
    mock_module.bin_path = '/usr/bin/ohai'
    mock_module.run_command_result = (0, '{"key": "value"}', '')
    output = collector.get_ohai_output(mock_module)
    assert output == '{"key": "value"}'

def test_get_ohai_output_no_ohai_path(mock_module):
    collector = OhaiFactCollector()
    mock_module.bin_path = None
    output = collector.get_ohai_output(mock_module)
    assert output is None

def test_get_ohai_output_command_failure(mock_module):
    collector = OhaiFactCollector()
    mock_module.bin_path = '/usr/bin/ohai'
    mock_module.run_command_result = (1, '', 'error')
    output = collector.get_ohai_output(mock_module)
    assert output is None

def test_collect_no_module():
    collector = OhaiFactCollector()
    facts = collector.collect()
    assert facts == {}

def test_collect_no_ohai_output(mock_module):
    collector = OhaiFactCollector()
    mock_module.bin_path = '/usr/bin/ohai'
    mock_module.run_command_result = (1, '', 'error')
    facts = collector.collect(module=mock_module)
    assert facts == {}

def test_collect_with_ohai_output(mock_module):
    collector = OhaiFactCollector()
    mock_module.bin_path = '/usr/bin/ohai'
    mock_module.run_command_result = (0, '{"key": "value"}', '')
    facts = collector.collect(module=mock_module)
    assert facts == {"key": "value"}

def test_collect_invalid_json(mock_module):
    collector = OhaiFactCollector()
    mock_module.bin_path = '/usr/bin/ohai'
    mock_module.run_command_result = (0, 'invalid json', '')
    facts = collector.collect(module=mock_module)
    assert facts == {}
