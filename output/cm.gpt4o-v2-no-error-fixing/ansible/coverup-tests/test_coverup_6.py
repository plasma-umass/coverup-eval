# file: lib/ansible/executor/powershell/module_manifest.py:79-140
# asked: {"lines": [79, 80, 81, 82, 83, 85, 87, 88, 91, 93, 96, 98, 101, 102, 103, 104, 105, 108, 109, 110, 112, 113, 115, 117, 118, 119, 120, 122, 123, 124, 127, 128, 129, 130, 132, 133, 134, 135, 139, 140], "branches": [[82, 83], [82, 85], [87, 88], [87, 96], [101, 102], [101, 139], [102, 103], [102, 117], [103, 102], [103, 104], [105, 103], [105, 108], [112, 113], [112, 115], [117, 118], [117, 132], [119, 120], [119, 122], [123, 124], [123, 127], [127, 128], [127, 132], [129, 130], [129, 132], [132, 101], [132, 133], [134, 101], [134, 135], [139, 0], [139, 140]]}
# gained: {"lines": [79, 80, 81, 82, 83, 85, 87, 88, 91, 93, 96, 98, 101, 102, 103, 104, 105, 108, 109, 110, 112, 113, 115, 117, 118, 119, 122, 123, 127, 128, 129, 132, 133, 134, 139, 140], "branches": [[82, 83], [82, 85], [87, 88], [87, 96], [101, 102], [101, 139], [102, 103], [102, 117], [103, 102], [103, 104], [105, 103], [105, 108], [112, 113], [117, 118], [117, 132], [119, 122], [123, 127], [127, 128], [129, 132], [132, 101], [132, 133], [134, 101], [139, 0], [139, 140]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.executor.powershell.module_manifest import PSModuleDepFinder

@pytest.fixture
def ps_module_dep_finder():
    return PSModuleDepFinder()

def test_scan_module_powershell(ps_module_dep_finder):
    module_data = b"#Requires -Module Ansible.ModuleUtils.TestModule\n#AnsibleRequires -Powershell Ansible.TestModule"
    ps_module_dep_finder._re_ps_module = [MagicMock()]
    ps_module_dep_finder._re_ps_module[0].match = MagicMock(return_value=MagicMock(group=MagicMock(return_value="Ansible.ModuleUtils.TestModule"), groupdict=MagicMock(return_value={})))
    ps_module_dep_finder.ps_modules = {}
    ps_module_dep_finder._re_cs_in_ps_module = [MagicMock()]
    ps_module_dep_finder._re_cs_in_ps_module[0].match = MagicMock(return_value=None)
    ps_module_dep_finder.cs_utils_module = {}
    ps_module_dep_finder._re_ps_version = MagicMock()
    ps_module_dep_finder._re_ps_version.match = MagicMock(return_value=None)
    ps_module_dep_finder._re_os_version = MagicMock()
    ps_module_dep_finder._re_os_version.match = MagicMock(return_value=None)
    ps_module_dep_finder.become = False
    ps_module_dep_finder._re_become = MagicMock()
    ps_module_dep_finder._re_become.match = MagicMock(return_value=None)
    ps_module_dep_finder._re_wrapper = MagicMock()
    ps_module_dep_finder._re_wrapper.match = MagicMock(return_value=None)
    ps_module_dep_finder._add_module = MagicMock()

    ps_module_dep_finder.scan_module(module_data, powershell=True)

    ps_module_dep_finder._re_ps_module[0].match.assert_called()
    ps_module_dep_finder._add_module.assert_called()

def test_scan_module_wrapper(ps_module_dep_finder):
    module_data = b"#Requires -Module Ansible.ModuleUtils.TestModule\n#AnsibleRequires -CSharpUtil Ansible.TestModule"
    ps_module_dep_finder._re_ps_module = [MagicMock()]
    ps_module_dep_finder._re_ps_module[0].match = MagicMock(return_value=None)
    ps_module_dep_finder.ps_modules = {}
    ps_module_dep_finder._re_cs_in_ps_module = [MagicMock()]
    ps_module_dep_finder._re_cs_in_ps_module[0].match = MagicMock(return_value=MagicMock(group=MagicMock(return_value="Ansible.ModuleUtils.TestModule"), groupdict=MagicMock(return_value={})))
    ps_module_dep_finder.cs_utils_module = {}
    ps_module_dep_finder._re_ps_version = MagicMock()
    ps_module_dep_finder._re_ps_version.match = MagicMock(return_value=None)
    ps_module_dep_finder._re_os_version = MagicMock()
    ps_module_dep_finder._re_os_version.match = MagicMock(return_value=None)
    ps_module_dep_finder.become = False
    ps_module_dep_finder._re_become = MagicMock()
    ps_module_dep_finder._re_become.match = MagicMock(return_value=None)
    ps_module_dep_finder._re_wrapper = MagicMock()
    ps_module_dep_finder._re_wrapper.match = MagicMock(return_value=None)
    ps_module_dep_finder._add_module = MagicMock()

    ps_module_dep_finder.scan_module(module_data, wrapper=True)

    ps_module_dep_finder._re_cs_in_ps_module[0].match.assert_called()
    ps_module_dep_finder._add_module.assert_called()

def test_scan_module_cs(ps_module_dep_finder):
    module_data = b"using Ansible.ModuleUtils.TestModule;"
    ps_module_dep_finder._re_cs_module = [MagicMock()]
    ps_module_dep_finder._re_cs_module[0].match = MagicMock(return_value=MagicMock(group=MagicMock(return_value="Ansible.ModuleUtils.TestModule"), groupdict=MagicMock(return_value={})))
    ps_module_dep_finder.cs_utils_module = {}
    ps_module_dep_finder._re_ps_version = MagicMock()
    ps_module_dep_finder._re_ps_version.match = MagicMock(return_value=None)
    ps_module_dep_finder._re_os_version = MagicMock()
    ps_module_dep_finder._re_os_version.match = MagicMock(return_value=None)
    ps_module_dep_finder.become = False
    ps_module_dep_finder._re_become = MagicMock()
    ps_module_dep_finder._re_become.match = MagicMock(return_value=None)
    ps_module_dep_finder._re_wrapper = MagicMock()
    ps_module_dep_finder._re_wrapper.match = MagicMock(return_value=None)
    ps_module_dep_finder._add_module = MagicMock()

    ps_module_dep_finder.scan_module(module_data, powershell=False)

    ps_module_dep_finder._re_cs_module[0].match.assert_called()
    ps_module_dep_finder._add_module.assert_called()
