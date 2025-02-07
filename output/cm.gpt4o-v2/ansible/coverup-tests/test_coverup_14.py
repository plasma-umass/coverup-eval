# file: lib/ansible/executor/powershell/module_manifest.py:79-140
# asked: {"lines": [79, 80, 81, 82, 83, 85, 87, 88, 91, 93, 96, 98, 101, 102, 103, 104, 105, 108, 109, 110, 112, 113, 115, 117, 118, 119, 120, 122, 123, 124, 127, 128, 129, 130, 132, 133, 134, 135, 139, 140], "branches": [[82, 83], [82, 85], [87, 88], [87, 96], [101, 102], [101, 139], [102, 103], [102, 117], [103, 102], [103, 104], [105, 103], [105, 108], [112, 113], [112, 115], [117, 118], [117, 132], [119, 120], [119, 122], [123, 124], [123, 127], [127, 128], [127, 132], [129, 130], [129, 132], [132, 101], [132, 133], [134, 101], [134, 135], [139, 0], [139, 140]]}
# gained: {"lines": [79, 80, 81, 82, 83, 85, 87, 88, 91, 93, 96, 98, 101, 102, 103, 104, 105, 108, 109, 110, 112, 113, 115, 117, 118, 119, 122, 123, 127, 128, 129, 132, 133, 134, 139, 140], "branches": [[82, 83], [82, 85], [87, 88], [87, 96], [101, 102], [101, 139], [102, 103], [102, 117], [103, 102], [103, 104], [105, 103], [105, 108], [112, 113], [117, 118], [117, 132], [119, 122], [123, 127], [127, 128], [129, 132], [132, 101], [132, 133], [134, 101], [139, 0], [139, 140]]}

import pytest
from unittest.mock import MagicMock

@pytest.fixture
def ps_module_dep_finder():
    from ansible.executor.powershell.module_manifest import PSModuleDepFinder
    return PSModuleDepFinder()

def test_scan_module_powershell(ps_module_dep_finder, mocker):
    module_data = b"#Requires -Module Ansible.ModuleUtils.TestModule\n#AnsibleRequires -Powershell Ansible.TestModule"
    mocker.patch.object(ps_module_dep_finder, '_re_ps_module', [mocker.Mock()])
    mocker.patch.object(ps_module_dep_finder, 'ps_modules', {})
    mocker.patch.object(ps_module_dep_finder, '_re_cs_in_ps_module', [mocker.Mock()])
    mocker.patch.object(ps_module_dep_finder, 'cs_utils_wrapper', {})
    mocker.patch.object(ps_module_dep_finder, 'cs_utils_module', {})
    mocker.patch.object(ps_module_dep_finder, '_re_ps_version', mocker.Mock())
    mocker.patch.object(ps_module_dep_finder, '_re_os_version', mocker.Mock())
    mocker.patch.object(ps_module_dep_finder, '_re_become', mocker.Mock())
    mocker.patch.object(ps_module_dep_finder, '_re_wrapper', mocker.Mock())
    mocker.patch.object(ps_module_dep_finder, 'scan_exec_script', mocker.Mock())
    mocker.patch.object(ps_module_dep_finder, '_add_module', mocker.Mock())
    mocker.patch.object(ps_module_dep_finder, 'become', False)

    ps_module_dep_finder._re_ps_module[0].match.return_value = mocker.Mock(group=lambda x: b"Ansible.ModuleUtils.TestModule", groupdict=lambda: {})
    ps_module_dep_finder._re_cs_in_ps_module[0].match.return_value = None
    ps_module_dep_finder._re_ps_version.match.return_value = None
    ps_module_dep_finder._re_os_version.match.return_value = None
    ps_module_dep_finder._re_become.match.return_value = None
    ps_module_dep_finder._re_wrapper.match.return_value = None

    ps_module_dep_finder.scan_module(module_data, powershell=True)

    assert ps_module_dep_finder._add_module.called

def test_scan_module_wrapper(ps_module_dep_finder, mocker):
    module_data = b"#AnsibleRequires -CSharpUtil Ansible.TestModule"
    mocker.patch.object(ps_module_dep_finder, '_re_ps_module', [mocker.Mock()])
    mocker.patch.object(ps_module_dep_finder, 'ps_modules', {})
    mocker.patch.object(ps_module_dep_finder, '_re_cs_in_ps_module', [mocker.Mock()])
    mocker.patch.object(ps_module_dep_finder, 'cs_utils_wrapper', {})
    mocker.patch.object(ps_module_dep_finder, 'cs_utils_module', {})
    mocker.patch.object(ps_module_dep_finder, '_re_ps_version', mocker.Mock())
    mocker.patch.object(ps_module_dep_finder, '_re_os_version', mocker.Mock())
    mocker.patch.object(ps_module_dep_finder, '_re_become', mocker.Mock())
    mocker.patch.object(ps_module_dep_finder, '_re_wrapper', mocker.Mock())
    mocker.patch.object(ps_module_dep_finder, 'scan_exec_script', mocker.Mock())
    mocker.patch.object(ps_module_dep_finder, '_add_module', mocker.Mock())
    mocker.patch.object(ps_module_dep_finder, 'become', False)

    ps_module_dep_finder._re_ps_module[0].match.return_value = None
    ps_module_dep_finder._re_cs_in_ps_module[0].match.return_value = mocker.Mock(group=lambda x: b"Ansible.TestModule", groupdict=lambda: {})
    ps_module_dep_finder._re_ps_version.match.return_value = None
    ps_module_dep_finder._re_os_version.match.return_value = None
    ps_module_dep_finder._re_become.match.return_value = None
    ps_module_dep_finder._re_wrapper.match.return_value = None

    ps_module_dep_finder.scan_module(module_data, wrapper=True)

    assert ps_module_dep_finder._add_module.called

def test_scan_module_cs(ps_module_dep_finder, mocker):
    module_data = b"using Ansible.TestModule;"
    mocker.patch.object(ps_module_dep_finder, '_re_ps_module', [mocker.Mock()])
    mocker.patch.object(ps_module_dep_finder, 'ps_modules', {})
    mocker.patch.object(ps_module_dep_finder, '_re_cs_in_ps_module', [mocker.Mock()])
    mocker.patch.object(ps_module_dep_finder, 'cs_utils_wrapper', {})
    mocker.patch.object(ps_module_dep_finder, 'cs_utils_module', {})
    mocker.patch.object(ps_module_dep_finder, '_re_cs_module', [mocker.Mock()])
    mocker.patch.object(ps_module_dep_finder, '_re_ps_version', mocker.Mock())
    mocker.patch.object(ps_module_dep_finder, '_re_os_version', mocker.Mock())
    mocker.patch.object(ps_module_dep_finder, '_re_become', mocker.Mock())
    mocker.patch.object(ps_module_dep_finder, '_re_wrapper', mocker.Mock())
    mocker.patch.object(ps_module_dep_finder, 'scan_exec_script', mocker.Mock())
    mocker.patch.object(ps_module_dep_finder, '_add_module', mocker.Mock())
    mocker.patch.object(ps_module_dep_finder, 'become', False)

    ps_module_dep_finder._re_cs_module[0].match.return_value = mocker.Mock(group=lambda x: b"Ansible.TestModule", groupdict=lambda: {})
    ps_module_dep_finder._re_ps_module[0].match.return_value = None
    ps_module_dep_finder._re_cs_in_ps_module[0].match.return_value = None
    ps_module_dep_finder._re_ps_version.match.return_value = None
    ps_module_dep_finder._re_os_version.match.return_value = None
    ps_module_dep_finder._re_become.match.return_value = None
    ps_module_dep_finder._re_wrapper.match.return_value = None

    ps_module_dep_finder.scan_module(module_data, powershell=False)

    assert ps_module_dep_finder._add_module.called
