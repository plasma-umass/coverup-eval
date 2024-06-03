# file lib/ansible/executor/powershell/module_manifest.py:27-77
# lines [27, 29, 30, 35, 36, 38, 39, 40, 42, 45, 49, 55, 60, 63, 69, 74, 75, 76, 77]
# branches []

import pytest
import re
from ansible.executor.powershell.module_manifest import PSModuleDepFinder

@pytest.fixture
def ps_module_dep_finder():
    return PSModuleDepFinder()

def test_ps_module_dep_finder_initialization(ps_module_dep_finder):
    assert ps_module_dep_finder.ps_modules == {}
    assert ps_module_dep_finder.exec_scripts == {}
    assert ps_module_dep_finder.cs_utils_wrapper == {}
    assert ps_module_dep_finder.cs_utils_module == {}
    assert ps_module_dep_finder.ps_version is None
    assert ps_module_dep_finder.os_version is None
    assert ps_module_dep_finder.become is False

    assert len(ps_module_dep_finder._re_cs_module) == 1
    assert len(ps_module_dep_finder._re_cs_in_ps_module) == 1
    assert len(ps_module_dep_finder._re_ps_module) == 2

    assert ps_module_dep_finder._re_wrapper.pattern == to_bytes(r'(?i)^#\s*ansiblerequires\s+-wrapper\s+(\w*)')
    assert ps_module_dep_finder._re_ps_version.pattern == to_bytes(r'(?i)^#requires\s+\-version\s+([0-9]+(\.[0-9]+){0,3})$')
    assert ps_module_dep_finder._re_os_version.pattern == to_bytes(r'(?i)^#ansiblerequires\s+\-osversion\s+([0-9]+(\.[0-9]+){0,3})$')
    assert ps_module_dep_finder._re_become.pattern == to_bytes(r'(?i)^#ansiblerequires\s+\-become$')

def to_bytes(string):
    return string.encode('utf-8')
