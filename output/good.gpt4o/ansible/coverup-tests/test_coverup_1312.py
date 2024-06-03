# file lib/ansible/module_utils/facts/system/lsb.py:80-106
# lines []
# branches ['98->101', '102->101']

import pytest
from unittest.mock import Mock, patch

# Assuming the LSBFactCollector and BaseFactCollector are imported from the module
from ansible.module_utils.facts.system.lsb import LSBFactCollector

@pytest.fixture
def mock_module():
    module = Mock()
    module.get_bin_path = Mock(return_value=None)
    return module

@pytest.fixture
def lsb_collector():
    return LSBFactCollector()

def test_collect_with_release(mock_module, lsb_collector):
    # Mock the _lsb_release_file method to return a dict with 'release'
    with patch.object(lsb_collector, '_lsb_release_file', return_value={'release': '20.04'}):
        facts = lsb_collector.collect(module=mock_module)
        assert 'lsb' in facts
        assert 'release' in facts['lsb']
        assert 'major_release' in facts['lsb']
        assert facts['lsb']['major_release'] == '20'

def test_collect_with_strip_quotes(mock_module, lsb_collector):
    # Mock the _lsb_release_file method to return a dict with a value that needs stripping
    with patch.object(lsb_collector, '_lsb_release_file', return_value={'release': '20.04', 'description': ' "Ubuntu" '}):
        with patch.object(LSBFactCollector, 'STRIP_QUOTES', ' "'):
            facts = lsb_collector.collect(module=mock_module)
            assert 'lsb' in facts
            assert 'release' in facts['lsb']
            assert 'description' in facts['lsb']
            assert facts['lsb']['description'] == 'Ubuntu'

def test_collect_with_empty_values(mock_module, lsb_collector):
    # Mock the _lsb_release_file method to return a dict with empty values
    with patch.object(lsb_collector, '_lsb_release_file', return_value={'release': '20.04', 'description': ''}):
        with patch.object(LSBFactCollector, 'STRIP_QUOTES', ' "'):
            facts = lsb_collector.collect(module=mock_module)
            assert 'lsb' in facts
            assert 'release' in facts['lsb']
            assert 'description' in facts['lsb']
            assert facts['lsb']['description'] == ''
