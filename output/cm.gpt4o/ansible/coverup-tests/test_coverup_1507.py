# file lib/ansible/module_utils/facts/system/lsb.py:80-106
# lines []
# branches ['98->101']

import pytest
from unittest.mock import Mock, patch

# Assuming the LSBFactCollector and BaseFactCollector are imported from the module
from ansible.module_utils.facts.system.lsb import LSBFactCollector

@pytest.fixture
def mock_module():
    module = Mock()
    module.get_bin_path.return_value = '/usr/bin/lsb_release'
    return module

@pytest.fixture
def lsb_collector():
    return LSBFactCollector()

def test_collect_with_release(mock_module, lsb_collector):
    with patch.object(lsb_collector, '_lsb_release_bin', return_value={'release': '20.04'}):
        with patch.object(lsb_collector, '_lsb_release_file', return_value={}):
            facts = lsb_collector.collect(module=mock_module)
            assert 'lsb' in facts
            assert 'release' in facts['lsb']
            assert 'major_release' in facts['lsb']
            assert facts['lsb']['major_release'] == '20'

def test_collect_without_release(mock_module, lsb_collector):
    with patch.object(lsb_collector, '_lsb_release_bin', return_value={}):
        with patch.object(lsb_collector, '_lsb_release_file', return_value={'release': '18.04'}):
            facts = lsb_collector.collect(module=mock_module)
            assert 'lsb' in facts
            assert 'release' in facts['lsb']
            assert 'major_release' in facts['lsb']
            assert facts['lsb']['major_release'] == '18'

def test_collect_strip_quotes(mock_module, lsb_collector):
    with patch.object(lsb_collector, '_lsb_release_bin', return_value={'release': '20.04', 'description': '"Ubuntu 20.04 LTS"'}):
        with patch.object(lsb_collector, '_lsb_release_file', return_value={}):
            facts = lsb_collector.collect(module=mock_module)
            assert 'lsb' in facts
            assert 'release' in facts['lsb']
            assert 'description' in facts['lsb']
            assert facts['lsb']['description'] == 'Ubuntu 20.04 LTS'
            assert 'major_release' in facts['lsb']
            assert facts['lsb']['major_release'] == '20'

def test_collect_no_release(mock_module, lsb_collector):
    with patch.object(lsb_collector, '_lsb_release_bin', return_value={}):
        with patch.object(lsb_collector, '_lsb_release_file', return_value={}):
            facts = lsb_collector.collect(module=mock_module)
            assert 'lsb' in facts
            assert 'release' not in facts['lsb']
            assert 'major_release' not in facts['lsb']
