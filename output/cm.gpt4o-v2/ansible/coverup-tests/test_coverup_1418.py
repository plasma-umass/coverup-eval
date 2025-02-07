# file: lib/ansible/module_utils/facts/system/lsb.py:80-106
# asked: {"lines": [], "branches": [[98, 101], [102, 101]]}
# gained: {"lines": [], "branches": [[98, 101]]}

import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.facts.system.lsb import LSBFactCollector

@pytest.fixture
def mock_module():
    return Mock()

def test_collect_with_release(mock_module):
    collector = LSBFactCollector()
    mock_module.get_bin_path.return_value = '/usr/bin/lsb_release'
    mock_module.run_command.return_value = (0, 'Release: 20.04\n', '')

    with patch.object(LSBFactCollector, '_lsb_release_bin', return_value={'release': '20.04'}):
        facts = collector.collect(module=mock_module)
        assert 'lsb' in facts
        assert facts['lsb']['major_release'] == '20'

def test_collect_without_release(mock_module):
    collector = LSBFactCollector()
    mock_module.get_bin_path.return_value = None

    with patch.object(LSBFactCollector, '_lsb_release_file', return_value={'id': 'Ubuntu'}):
        facts = collector.collect(module=mock_module)
        assert 'lsb' in facts
        assert 'major_release' not in facts['lsb']

def test_collect_strip_quotes(mock_module):
    collector = LSBFactCollector()
    mock_module.get_bin_path.return_value = '/usr/bin/lsb_release'
    mock_module.run_command.return_value = (0, 'Release: "20.04"\n', '')

    with patch.object(LSBFactCollector, '_lsb_release_bin', return_value={'release': '"20.04"'}):
        facts = collector.collect(module=mock_module)
        assert 'lsb' in facts
        assert facts['lsb']['release'] == '20.04'
