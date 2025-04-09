# file: lib/ansible/executor/powershell/module_manifest.py:27-77
# asked: {"lines": [27, 29, 30, 35, 36, 38, 39, 40, 42, 45, 49, 55, 60, 63, 69, 74, 75, 76, 77], "branches": []}
# gained: {"lines": [27, 29, 30, 35, 36, 38, 39, 40, 42, 45, 49, 55, 60, 63, 69, 74, 75, 76, 77], "branches": []}

import pytest
import re
from ansible.module_utils._text import to_bytes
from ansible.executor.powershell.module_manifest import PSModuleDepFinder

@pytest.fixture
def ps_module_dep_finder():
    return PSModuleDepFinder()

def test_init(ps_module_dep_finder):
    assert ps_module_dep_finder.ps_modules == {}
    assert ps_module_dep_finder.exec_scripts == {}
    assert ps_module_dep_finder.cs_utils_wrapper == {}
    assert ps_module_dep_finder.cs_utils_module == {}
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
