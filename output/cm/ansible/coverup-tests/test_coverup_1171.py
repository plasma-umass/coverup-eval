# file lib/ansible/module_utils/facts/system/lsb.py:80-106
# lines [87, 90, 91, 92, 95, 96, 98, 99, 101, 102, 103, 105, 106]
# branches ['84->87', '90->91', '90->95', '95->96', '95->98', '98->99', '98->101', '101->102', '101->105', '102->101', '102->103']

import pytest
from ansible.module_utils.facts.system.lsb import LSBFactCollector

@pytest.fixture
def mock_module(mocker):
    mock = mocker.MagicMock()
    mock.get_bin_path.return_value = None
    return mock

def test_lsb_fact_collector_with_no_lsb_release_bin(mock_module):
    collector = LSBFactCollector()
    facts = collector.collect(module=mock_module)
    assert 'lsb' in facts
    assert 'release' not in facts['lsb']
    assert mock_module.get_bin_path.called_with('lsb_release')

def test_lsb_fact_collector_with_lsb_release_bin(mock_module, mocker):
    mock_module.get_bin_path.return_value = '/usr/bin/lsb_release'
    mocker.patch('ansible.module_utils.facts.system.lsb.LSBFactCollector._lsb_release_bin', return_value={'release': '1.2.3'})
    collector = LSBFactCollector()
    facts = collector.collect(module=mock_module)
    assert 'lsb' in facts
    assert 'release' in facts['lsb']
    assert facts['lsb']['release'] == '1.2.3'
    assert facts['lsb']['major_release'] == '1'
    assert mock_module.get_bin_path.called_with('lsb_release')

def test_lsb_fact_collector_with_lsb_release_file(mock_module, mocker):
    mocker.patch('ansible.module_utils.facts.system.lsb.LSBFactCollector._lsb_release_file', return_value={'release': '4.5.6'})
    collector = LSBFactCollector()
    facts = collector.collect(module=mock_module)
    assert 'lsb' in facts
    assert 'release' in facts['lsb']
    assert facts['lsb']['release'] == '4.5.6'
    assert facts['lsb']['major_release'] == '4'
    assert mock_module.get_bin_path.called_with('lsb_release')
