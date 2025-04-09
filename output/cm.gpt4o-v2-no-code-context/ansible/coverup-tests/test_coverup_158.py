# file: lib/ansible/executor/powershell/module_manifest.py:27-77
# asked: {"lines": [27, 29, 30, 35, 36, 38, 39, 40, 42, 45, 49, 55, 60, 63, 69, 74, 75, 76, 77], "branches": []}
# gained: {"lines": [27, 29, 30, 35, 36, 38, 39, 40, 42, 45, 49, 55, 60, 63, 69, 74, 75, 76, 77], "branches": []}

import pytest
import re
from ansible.executor.powershell.module_manifest import PSModuleDepFinder

@pytest.fixture
def ps_module_dep_finder():
    return PSModuleDepFinder()

def test_ps_module_dep_finder_initialization(ps_module_dep_finder):
    assert isinstance(ps_module_dep_finder.ps_modules, dict)
    assert isinstance(ps_module_dep_finder.exec_scripts, dict)
    assert isinstance(ps_module_dep_finder.cs_utils_wrapper, dict)
    assert isinstance(ps_module_dep_finder.cs_utils_module, dict)
    assert ps_module_dep_finder.ps_version is None
    assert ps_module_dep_finder.os_version is None
    assert ps_module_dep_finder.become is False

    assert len(ps_module_dep_finder._re_cs_module) == 1
    assert isinstance(ps_module_dep_finder._re_cs_module[0], re.Pattern)

    assert len(ps_module_dep_finder._re_cs_in_ps_module) == 1
    assert isinstance(ps_module_dep_finder._re_cs_in_ps_module[0], re.Pattern)

    assert len(ps_module_dep_finder._re_ps_module) == 2
    assert isinstance(ps_module_dep_finder._re_ps_module[0], re.Pattern)
    assert isinstance(ps_module_dep_finder._re_ps_module[1], re.Pattern)

    assert isinstance(ps_module_dep_finder._re_wrapper, re.Pattern)
    assert isinstance(ps_module_dep_finder._re_ps_version, re.Pattern)
    assert isinstance(ps_module_dep_finder._re_os_version, re.Pattern)
    assert isinstance(ps_module_dep_finder._re_become, re.Pattern)

def test_re_cs_module(ps_module_dep_finder):
    match = ps_module_dep_finder._re_cs_module[0].match(b'using Ansible.SomeModule;')
    assert match is not None

def test_re_cs_in_ps_module(ps_module_dep_finder):
    match = ps_module_dep_finder._re_cs_in_ps_module[0].match(b'#AnsibleRequires -CSharpUtil Ansible.SomeModule')
    assert match is not None

def test_re_ps_module(ps_module_dep_finder):
    match = ps_module_dep_finder._re_ps_module[0].match(b'#Requires -Module Ansible.ModuleUtils.SomeModule')
    assert match is not None

    match = ps_module_dep_finder._re_ps_module[1].match(b'#AnsibleRequires -PowerShell Ansible.ModuleUtils.SomeModule')
    assert match is not None

def test_re_wrapper(ps_module_dep_finder):
    match = ps_module_dep_finder._re_wrapper.match(b'#AnsibleRequires -Wrapper SomeWrapper')
    assert match is not None

def test_re_ps_version(ps_module_dep_finder):
    match = ps_module_dep_finder._re_ps_version.match(b'#Requires -Version 5.1')
    assert match is not None

def test_re_os_version(ps_module_dep_finder):
    match = ps_module_dep_finder._re_os_version.match(b'#AnsibleRequires -OSVersion 10.0.17763')
    assert match is not None

def test_re_become(ps_module_dep_finder):
    match = ps_module_dep_finder._re_become.match(b'#AnsibleRequires -Become')
    assert match is not None
