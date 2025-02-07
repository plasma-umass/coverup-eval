# file: lib/ansible/executor/powershell/module_manifest.py:79-140
# asked: {"lines": [120, 124, 130, 135], "branches": [[112, 115], [119, 120], [123, 124], [127, 132], [129, 130], [134, 135]]}
# gained: {"lines": [120, 124, 130, 135], "branches": [[119, 120], [123, 124], [127, 132], [129, 130], [134, 135]]}

import pytest
from unittest.mock import MagicMock
from ansible.executor.powershell.module_manifest import PSModuleDepFinder

@pytest.fixture
def ps_module_dep_finder():
    finder = PSModuleDepFinder()
    finder._re_ps_module = [MagicMock()]
    finder.ps_modules = {}
    finder._re_cs_in_ps_module = [MagicMock()]
    finder.cs_utils_wrapper = {}
    finder._re_cs_module = [MagicMock()]
    finder.cs_utils_module = {}
    finder._re_ps_version = MagicMock()
    finder._re_os_version = MagicMock()
    finder.become = False
    finder._re_become = MagicMock()
    finder._re_wrapper = MagicMock()
    finder.scan_exec_script = MagicMock()
    finder._add_module = MagicMock()
    finder._parse_version_match = MagicMock()
    return finder

def test_scan_module_all_branches(ps_module_dep_finder):
    module_data = b"#Requires -Module Ansible.ModuleUtils.Test\n#AnsibleRequires -Powershell Ansible.Test\n#AnsibleRequires -CSharpUtil Ansible.Test\n#Requires -Version 5.1\n#Requires -OS Windows\n#Requires -Become\n#Requires -Wrapper TestWrapper"
    ps_module_dep_finder._re_ps_module[0].match.side_effect = [MagicMock(), None, None, None, None, None, None]
    ps_module_dep_finder._re_cs_in_ps_module[0].match.side_effect = [None, MagicMock(), None, None, None, None, None]
    ps_module_dep_finder._re_cs_module[0].match.side_effect = [None, None, MagicMock(), None, None, None, None]
    ps_module_dep_finder._re_ps_version.match.side_effect = [None, None, None, MagicMock(), None, None, None]
    ps_module_dep_finder._re_os_version.match.side_effect = [None, None, None, None, MagicMock(), None, None]
    ps_module_dep_finder._re_become.match.side_effect = [None, None, None, None, None, MagicMock(), None]
    ps_module_dep_finder._re_wrapper.match.side_effect = [None, None, None, None, None, None, MagicMock()]

    ps_module_dep_finder.scan_module(module_data, wrapper=True)

    assert ps_module_dep_finder._parse_version_match.call_count == 2
    assert ps_module_dep_finder.become is True
    ps_module_dep_finder.scan_exec_script.assert_called_once()
