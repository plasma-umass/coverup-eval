# file lib/ansible/module_utils/facts/system/lsb.py:32-58
# lines [32, 33, 35, 36, 38, 39, 40, 42, 43, 44, 45, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 58]
# branches ['35->36', '35->38', '39->40', '39->42', '42->43', '42->58', '43->44', '43->45', '47->48', '47->49', '49->50', '49->51', '51->52', '51->53', '53->54', '53->55', '55->42', '55->56']

import pytest
from ansible.module_utils.facts.system.lsb import LSBFactCollector

@pytest.fixture
def mock_module(mocker):
    mock_module = mocker.MagicMock()
    mock_module.run_command = mocker.MagicMock()
    return mock_module

def test_lsb_release_bin_success(mock_module):
    lsb_path = '/usr/bin/lsb_release'
    mock_module.run_command.return_value = (0, "LSB Version: 1.4\nDistributor ID: Test\nDescription: Test Description\nRelease: 1.0\nCodename: TestCodename", "")
    
    lsb_collector = LSBFactCollector()
    lsb_facts = lsb_collector._lsb_release_bin(lsb_path, mock_module)
    
    assert lsb_facts['release'] == '1.0'
    assert lsb_facts['id'] == 'Test'
    assert lsb_facts['description'] == 'Test Description'
    assert lsb_facts['codename'] == 'TestCodename'
    mock_module.run_command.assert_called_once_with([lsb_path, "-a"], errors='surrogate_then_replace')

def test_lsb_release_bin_failure(mock_module):
    lsb_path = '/usr/bin/lsb_release'
    mock_module.run_command.return_value = (1, "", "Error")
    
    lsb_collector = LSBFactCollector()
    lsb_facts = lsb_collector._lsb_release_bin(lsb_path, mock_module)
    
    assert lsb_facts == {}
    mock_module.run_command.assert_called_once_with([lsb_path, "-a"], errors='surrogate_then_replace')

def test_lsb_release_bin_no_lsb_path(mock_module):
    lsb_path = None
    
    lsb_collector = LSBFactCollector()
    lsb_facts = lsb_collector._lsb_release_bin(lsb_path, mock_module)
    
    assert lsb_facts == {}
    mock_module.run_command.assert_not_called()

def test_lsb_release_bin_invalid_output(mock_module):
    lsb_path = '/usr/bin/lsb_release'
    mock_module.run_command.return_value = (0, "Invalid output", "")
    
    lsb_collector = LSBFactCollector()
    lsb_facts = lsb_collector._lsb_release_bin(lsb_path, mock_module)
    
    assert lsb_facts == {}
    mock_module.run_command.assert_called_once_with([lsb_path, "-a"], errors='surrogate_then_replace')
