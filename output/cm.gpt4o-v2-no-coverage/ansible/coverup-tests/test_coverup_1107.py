# file: lib/ansible/executor/powershell/module_manifest.py:79-140
# asked: {"lines": [85, 96, 98, 108, 109, 110, 112, 113, 115, 120, 124, 130, 135, 140], "branches": [[82, 85], [87, 96], [105, 108], [112, 113], [112, 115], [117, 132], [119, 120], [123, 124], [127, 132], [129, 130], [132, 101], [134, 135], [139, 140]]}
# gained: {"lines": [85, 96, 98, 108, 109, 110, 112, 113, 115, 120, 124, 130, 135, 140], "branches": [[82, 85], [87, 96], [105, 108], [112, 113], [117, 132], [119, 120], [123, 124], [127, 132], [129, 130], [132, 101], [134, 135], [139, 140]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.executor.powershell.module_manifest import PSModuleDepFinder

@pytest.fixture
def ps_module_dep_finder():
    finder = PSModuleDepFinder()
    finder._re_ps_module = [MagicMock()]
    finder.ps_modules = {}
    finder._re_cs_in_ps_module = [MagicMock()]
    finder.cs_utils_wrapper = {}
    finder.cs_utils_module = {}
    finder._re_cs_module = [MagicMock()]
    finder._re_ps_version = MagicMock()
    finder._re_os_version = MagicMock()
    finder._re_become = MagicMock()
    finder._re_wrapper = MagicMock()
    finder.exec_scripts = {}
    finder.become = False
    return finder

def test_scan_module_powershell(ps_module_dep_finder):
    module_data = b"#Requires -Module Ansible.ModuleUtils.Test\n#AnsibleRequires -Powershell Ansible.TestModule\n#AnsibleRequires -CSharpUtil Ansible.CSharpUtil\n#Requires -Version 5.1\n#Requires -OSVersion 10.0.14393.0\n#Requires -RunAsAdministrator\n#Requires -Wrapper TestWrapper"
    ps_module_dep_finder._re_ps_module[0].match.side_effect = [MagicMock(group=lambda x: b"Ansible.ModuleUtils.Test", groupdict=lambda: {}),
                                                              None, None, None, None, None, None]
    ps_module_dep_finder._re_cs_in_ps_module[0].match.side_effect = [None, MagicMock(group=lambda x: b"Ansible.CSharpUtil", groupdict=lambda: {}),
                                                                     None, None, None, None, None]
    ps_module_dep_finder._re_ps_version.match.side_effect = [None, None, MagicMock(group=lambda x: b"5.1"), None, None, None, None]
    ps_module_dep_finder._re_os_version.match.side_effect = [None, None, None, MagicMock(group=lambda x: b"10.0.14393.0"), None, None, None]
    ps_module_dep_finder._re_become.match.side_effect = [None, None, None, None, MagicMock(), None, None]
    ps_module_dep_finder._re_wrapper.match.side_effect = [None, None, None, None, None, MagicMock(group=lambda x: b"TestWrapper"), None]

    with patch.object(ps_module_dep_finder, '_add_module') as mock_add_module, \
         patch.object(ps_module_dep_finder, '_parse_version_match') as mock_parse_version_match, \
         patch.object(ps_module_dep_finder, 'scan_exec_script') as mock_scan_exec_script:
        ps_module_dep_finder.scan_module(module_data, fqn="TestFQN", wrapper=True, powershell=True)

        assert mock_add_module.call_count == 2
        assert mock_parse_version_match.call_count == 2
        assert mock_scan_exec_script.call_count == 1
        assert ps_module_dep_finder.become is True

def test_scan_module_non_powershell(ps_module_dep_finder):
    module_data = b"using Ansible.TestModule;\nusing ansible_collections.ns.coll.plugins.module_utils.TestUtil;"
    ps_module_dep_finder._re_cs_module[0].match.return_value = MagicMock(group=lambda x: b"Ansible.TestModule", groupdict=lambda: {})

    with patch.object(ps_module_dep_finder, '_add_module') as mock_add_module:
        ps_module_dep_finder.scan_module(module_data, fqn="TestFQN", wrapper=False, powershell=False)

        assert mock_add_module.call_count == 1
