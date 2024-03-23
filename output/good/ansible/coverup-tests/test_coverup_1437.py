# file lib/ansible/module_utils/facts/system/lsb.py:32-58
# lines []
# branches ['55->42']

import pytest
from ansible.module_utils.facts.system.lsb import LSBFactCollector

@pytest.fixture
def mock_module(mocker):
    mock_module = mocker.MagicMock()
    # Include multiple lines with different keys to ensure the loop continues after 'Codename:'
    mock_module.run_command.return_value = (0, "Distributor ID: Ubuntu\nDescription: Ubuntu 20.04.1 LTS\nRelease: 20.04\nCodename: Focal\nExtra: Info", "")
    return mock_module

def test_lsb_release_bin_codename_and_loop_continuation(mock_module):
    lsb_collector = LSBFactCollector()
    lsb_facts = lsb_collector._lsb_release_bin('/usr/bin/lsb_release', mock_module)
    assert 'codename' in lsb_facts
    assert lsb_facts['codename'] == 'Focal'
    assert 'id' in lsb_facts
    assert lsb_facts['id'] == 'Ubuntu'
    assert 'description' in lsb_facts
    assert lsb_facts['description'] == 'Ubuntu 20.04.1 LTS'
    assert 'release' in lsb_facts
    assert lsb_facts['release'] == '20.04'
    mock_module.run_command.assert_called_once_with(['/usr/bin/lsb_release', '-a'], errors='surrogate_then_replace')
