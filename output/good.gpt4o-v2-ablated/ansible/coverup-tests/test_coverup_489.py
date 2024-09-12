# file: lib/ansible/module_utils/facts/system/lsb.py:80-106
# asked: {"lines": [81, 82, 84, 85, 87, 90, 91, 92, 95, 96, 98, 99, 101, 102, 103, 105, 106], "branches": [[84, 85], [84, 87], [90, 91], [90, 95], [95, 96], [95, 98], [98, 99], [98, 101], [101, 102], [101, 105], [102, 101], [102, 103]]}
# gained: {"lines": [81, 82, 84, 85, 87, 90, 91, 92, 95, 96, 98, 99, 101, 102, 103, 105, 106], "branches": [[84, 85], [84, 87], [90, 91], [90, 95], [95, 96], [95, 98], [98, 99], [98, 101], [101, 102], [101, 105], [102, 103]]}

import pytest
from unittest.mock import Mock, patch

# Assuming the LSBFactCollector and BaseFactCollector are defined in ansible/module_utils/facts/system/lsb.py
from ansible.module_utils.facts.system.lsb import LSBFactCollector

@pytest.fixture
def mock_module():
    return Mock()

@pytest.fixture
def lsb_collector():
    return LSBFactCollector()

def test_collect_no_module(lsb_collector):
    result = lsb_collector.collect()
    assert result == {}

def test_collect_no_lsb_release_bin_no_lsb_release_file(lsb_collector, mock_module):
    mock_module.get_bin_path.return_value = None
    with patch.object(lsb_collector, '_lsb_release_file', return_value={}):
        result = lsb_collector.collect(module=mock_module)
    assert result == {'lsb': {}}

def test_collect_with_lsb_release_bin(lsb_collector, mock_module):
    mock_module.get_bin_path.return_value = '/usr/bin/lsb_release'
    with patch.object(lsb_collector, '_lsb_release_bin', return_value={'release': '20.04'}):
        result = lsb_collector.collect(module=mock_module)
    assert result == {'lsb': {'release': '20.04', 'major_release': '20'}}

def test_collect_with_lsb_release_file(lsb_collector, mock_module):
    mock_module.get_bin_path.return_value = None
    with patch.object(lsb_collector, '_lsb_release_file', return_value={'release': '18.04'}):
        result = lsb_collector.collect(module=mock_module)
    assert result == {'lsb': {'release': '18.04', 'major_release': '18'}}

def test_collect_strip_quotes(lsb_collector, mock_module):
    mock_module.get_bin_path.return_value = '/usr/bin/lsb_release'
    with patch.object(lsb_collector, '_lsb_release_bin', return_value={'release': '20.04', 'description': '"Ubuntu 20.04"'}) as mock_lsb_bin:
        result = lsb_collector.collect(module=mock_module)
    assert result == {'lsb': {'release': '20.04', 'major_release': '20', 'description': 'Ubuntu 20.04'}}
