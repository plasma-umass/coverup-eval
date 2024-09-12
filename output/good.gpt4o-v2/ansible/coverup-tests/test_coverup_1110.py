# file: lib/ansible/module_utils/facts/system/lsb.py:80-106
# asked: {"lines": [81, 82, 84, 85, 87, 90, 91, 92, 95, 96, 98, 99, 101, 102, 103, 105, 106], "branches": [[84, 85], [84, 87], [90, 91], [90, 95], [95, 96], [95, 98], [98, 99], [98, 101], [101, 102], [101, 105], [102, 101], [102, 103]]}
# gained: {"lines": [81, 82, 84, 85, 87, 90, 91, 92, 95, 96, 98, 99, 101, 102, 103, 105, 106], "branches": [[84, 85], [84, 87], [90, 91], [90, 95], [95, 96], [95, 98], [98, 99], [101, 102], [101, 105], [102, 103]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.module_utils.facts.system.lsb import LSBFactCollector

@pytest.fixture
def mock_module():
    return MagicMock()

def test_collect_no_module():
    collector = LSBFactCollector()
    result = collector.collect()
    assert result == {}

def test_collect_with_lsb_release_bin(mock_module):
    collector = LSBFactCollector()
    mock_module.get_bin_path.return_value = '/usr/bin/lsb_release'
    with patch.object(collector, '_lsb_release_bin', return_value={'release': '20.04'}):
        result = collector.collect(module=mock_module)
    assert result == {'lsb': {'release': '20.04', 'major_release': '20'}}

def test_collect_with_lsb_release_file(mock_module):
    collector = LSBFactCollector()
    mock_module.get_bin_path.return_value = None
    with patch.object(collector, '_lsb_release_bin', return_value={}):
        with patch.object(collector, '_lsb_release_file', return_value={'release': '20.04'}):
            result = collector.collect(module=mock_module)
    assert result == {'lsb': {'release': '20.04', 'major_release': '20'}}

def test_collect_strip_quotes(mock_module):
    collector = LSBFactCollector()
    mock_module.get_bin_path.return_value = '/usr/bin/lsb_release'
    with patch.object(collector, '_lsb_release_bin', return_value={'release': '20.04', 'distributor_id': ' "Ubuntu" '}):
        result = collector.collect(module=mock_module)
    assert result == {'lsb': {'release': '20.04', 'major_release': '20', 'distributor_id': ' "Ubuntu" '.strip(LSBFactCollector.STRIP_QUOTES)}}
