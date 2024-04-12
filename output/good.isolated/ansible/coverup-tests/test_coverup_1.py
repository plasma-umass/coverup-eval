# file lib/ansible/module_utils/facts/system/service_mgr.py:65-150
# lines [65, 66, 68, 69, 71, 72, 78, 79, 80, 81, 82, 86, 87, 88, 92, 93, 96, 97, 99, 100, 102, 103, 104, 105, 107, 109, 112, 114, 117, 119, 120, 122, 123, 125, 126, 127, 128, 129, 130, 131, 132, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 145, 147, 149, 150]
# branches ['68->69', '68->71', '87->88', '87->96', '92->93', '92->96', '96->97', '96->99', '99->100', '99->102', '102->103', '102->107', '107->109', '107->112', '112->114', '112->117', '117->119', '117->123', '119->120', '119->122', '123->125', '123->126', '126->127', '126->128', '128->129', '128->130', '130->131', '130->132', '132->134', '132->145', '134->135', '134->136', '136->137', '136->138', '138->139', '138->140', '140->141', '140->142', '142->143', '142->145', '145->147', '145->149']

import os
import re
from distutils.version import LooseVersion
import platform
import pytest
from unittest.mock import MagicMock, mock_open, patch

# Assuming the ServiceMgrFactCollector class and its dependencies are defined elsewhere in the codebase
# and that the following imports would be valid in the context of the codebase:
from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector

@pytest.fixture
def mock_module():
    mock_mod = MagicMock()
    mock_mod.run_command.return_value = (0, 'init\n', '')
    return mock_mod

@pytest.fixture
def mock_collected_facts():
    return {
        'ansible_distribution': 'Linux',
        'ansible_system': 'Linux'
    }

def test_service_mgr_fact_collector(mock_module, mock_collected_facts):
    with patch('os.path.islink', return_value=False), \
         patch('os.path.exists', side_effect=lambda x: x in ['/etc/init.d/']), \
         patch('ansible.module_utils.facts.system.service_mgr.ServiceMgrFactCollector.is_systemd_managed', return_value=False), \
         patch('ansible.module_utils.facts.system.service_mgr.ServiceMgrFactCollector.is_systemd_managed_offline', return_value=False), \
         patch('ansible.module_utils.facts.system.service_mgr.get_file_content', return_value=None), \
         patch('os.readlink', return_value=''), \
         patch('os.path.basename', return_value='init'), \
         patch('ansible.module_utils.facts.system.service_mgr.to_native', side_effect=lambda x: x), \
         patch('platform.mac_ver', return_value=('10.3', ('', '', ''), '')):
        
        collector = ServiceMgrFactCollector()
        facts = collector.collect(module=mock_module, collected_facts=mock_collected_facts)
        
        assert facts['service_mgr'] == 'sysvinit', "Expected service manager to be 'sysvinit'"

        # Test the branch where 'ansible_distribution' is 'MacOSX' and version is less than '10.4'
        mock_collected_facts['ansible_distribution'] = 'MacOSX'
        facts = collector.collect(module=mock_module, collected_facts=mock_collected_facts)
        assert facts['service_mgr'] == 'systemstarter', "Expected service manager to be 'systemstarter'"

        # Cleanup after test
        mock_collected_facts['ansible_distribution'] = 'Linux'
