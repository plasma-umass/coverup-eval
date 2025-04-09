# file lib/ansible/executor/powershell/module_manifest.py:27-77
# lines [27, 29, 30, 35, 36, 38, 39, 40, 42, 45, 49, 55, 60, 63, 69, 74, 75, 76, 77]
# branches []

import pytest
import re
from ansible.executor.powershell.module_manifest import PSModuleDepFinder
from ansible.module_utils._text import to_bytes

@pytest.fixture
def ps_module_dep_finder():
    return PSModuleDepFinder()

def test_ps_module_dep_finder_regex_matches(ps_module_dep_finder):
    # Test the regex patterns to ensure they match the expected strings
    cs_module_match = ps_module_dep_finder._re_cs_module[0].match(
        to_bytes('using ansible_collections.namespace.collection.plugins.module_utils.name;')
    )
    assert cs_module_match is not None

    cs_in_ps_module_match = ps_module_dep_finder._re_cs_in_ps_module[0].match(
        to_bytes('#AnsibleRequires -CSharpUtil ansible_collections.namespace.collection.plugins.module_utils.name')
    )
    assert cs_in_ps_module_match is not None

    ps_module_match = ps_module_dep_finder._re_ps_module[0].match(
        to_bytes('#Requires -Module Ansible.ModuleUtils.name')
    )
    assert ps_module_match is not None

    ps_module_new_match = ps_module_dep_finder._re_ps_module[1].match(
        to_bytes('#AnsibleRequires -PowerShell Ansible.ModuleUtils.name')
    )
    assert ps_module_new_match is not None

    wrapper_match = ps_module_dep_finder._re_wrapper.match(
        to_bytes('#AnsibleRequires -wrapper wrapper_name')
    )
    assert wrapper_match is not None

    ps_version_match = ps_module_dep_finder._re_ps_version.match(
        to_bytes('#requires -version 5.1')
    )
    assert ps_version_match is not None

    os_version_match = ps_module_dep_finder._re_os_version.match(
        to_bytes('#AnsibleRequires -osversion 10.0.14393')
    )
    assert os_version_match is not None

    become_match = ps_module_dep_finder._re_become.match(
        to_bytes('#AnsibleRequires -become')
    )
    assert become_match is not None
