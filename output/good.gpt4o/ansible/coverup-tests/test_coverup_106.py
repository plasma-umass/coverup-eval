# file lib/ansible/module_utils/facts/system/lsb.py:80-106
# lines [80, 81, 82, 84, 85, 87, 90, 91, 92, 95, 96, 98, 99, 101, 102, 103, 105, 106]
# branches ['84->85', '84->87', '90->91', '90->95', '95->96', '95->98', '98->99', '98->101', '101->102', '101->105', '102->101', '102->103']

import pytest
from unittest.mock import MagicMock, patch

# Assuming the LSBFactCollector and BaseFactCollector are defined in ansible.module_utils.facts.system.lsb
from ansible.module_utils.facts.system.lsb import LSBFactCollector

@pytest.fixture
def mock_module():
    module = MagicMock()
    module.get_bin_path = MagicMock(return_value=None)
    return module

@pytest.fixture
def lsb_collector():
    return LSBFactCollector()

def test_collect_no_module(lsb_collector):
    result = lsb_collector.collect()
    assert result == {}

def test_collect_no_lsb_release_bin(mock_module, lsb_collector):
    with patch.object(lsb_collector, '_lsb_release_file', return_value={'release': '20.04'}):
        result = lsb_collector.collect(module=mock_module)
        assert 'lsb' in result
        assert result['lsb']['release'] == '20.04'
        assert result['lsb']['major_release'] == '20'

def test_collect_lsb_release_bin(mock_module, lsb_collector):
    mock_module.get_bin_path = MagicMock(return_value='/usr/bin/lsb_release')
    with patch.object(lsb_collector, '_lsb_release_bin', return_value={'release': '20.04'}):
        result = lsb_collector.collect(module=mock_module)
        assert 'lsb' in result
        assert result['lsb']['release'] == '20.04'
        assert result['lsb']['major_release'] == '20'

def test_collect_strip_quotes(mock_module, lsb_collector):
    mock_module.get_bin_path = MagicMock(return_value='/usr/bin/lsb_release')
    with patch.object(lsb_collector, '_lsb_release_bin', return_value={'release': '20.04', 'description': ' "Ubuntu 20.04" '}):
        with patch.object(LSBFactCollector, 'STRIP_QUOTES', ' "'):
            result = lsb_collector.collect(module=mock_module)
            assert 'lsb' in result
            assert result['lsb']['release'] == '20.04'
            assert result['lsb']['major_release'] == '20'
            assert result['lsb']['description'] == 'Ubuntu 20.04'
