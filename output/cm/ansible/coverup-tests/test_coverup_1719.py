# file lib/ansible/module_utils/facts/system/lsb.py:80-106
# lines []
# branches ['102->101']

import pytest
from ansible.module_utils.facts.system.lsb import LSBFactCollector

@pytest.fixture
def mock_module(mocker):
    mock = mocker.MagicMock()
    mock.get_bin_path.return_value = None
    return mock

def test_lsb_fact_collector_with_empty_and_quoted_values(mock_module, mocker):
    mock_lsb_facts = {'id': '"Ubuntu"', 'release': '"20.04"', 'codename': '', 'description': '"Ubuntu 20.04 LTS"'}
    mocker.patch.object(LSBFactCollector, '_lsb_release_file', return_value=mock_lsb_facts)
    
    fact_collector = LSBFactCollector()
    facts = fact_collector.collect(module=mock_module)
    
    assert 'lsb' in facts
    assert facts['lsb']['id'] == 'Ubuntu'
    assert facts['lsb']['release'] == '20.04'
    assert facts['lsb']['codename'] == ''
    assert facts['lsb']['description'] == 'Ubuntu 20.04 LTS'
    assert facts['lsb']['major_release'] == '20'
    
    # Verify that the branch 102->101 is executed
    for k, v in mock_lsb_facts.items():
        if v:
            assert facts['lsb'][k] == v.strip(LSBFactCollector.STRIP_QUOTES)
        else:
            assert facts['lsb'][k] == ''
