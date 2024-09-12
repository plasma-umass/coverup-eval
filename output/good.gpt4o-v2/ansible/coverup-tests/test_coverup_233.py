# file: lib/ansible/executor/powershell/module_manifest.py:237-251
# asked: {"lines": [237, 238, 242, 243, 245, 246, 247, 250, 251], "branches": [[242, 243], [242, 245], [246, 247], [246, 250], [250, 0], [250, 251]]}
# gained: {"lines": [237, 238, 242, 243, 245, 246, 247, 250, 251], "branches": [[242, 243], [242, 245], [246, 247], [246, 250], [250, 0], [250, 251]]}

import pytest
from unittest.mock import Mock
from ansible.executor.powershell.module_manifest import PSModuleDepFinder

@pytest.fixture
def ps_module_dep_finder():
    return PSModuleDepFinder()

def test_parse_version_match_new_version(ps_module_dep_finder):
    match = Mock()
    match.group.side_effect = ["1.0", None]
    ps_module_dep_finder._parse_version_match(match, 'ps_version')
    assert ps_module_dep_finder.ps_version == "1.0.0"

def test_parse_version_match_existing_version(ps_module_dep_finder):
    ps_module_dep_finder.ps_version = "1.0.0"
    match = Mock()
    match.group.side_effect = ["1.1", None]
    ps_module_dep_finder._parse_version_match(match, 'ps_version')
    assert ps_module_dep_finder.ps_version == "1.1.0"

def test_parse_version_match_lower_version(ps_module_dep_finder):
    ps_module_dep_finder.ps_version = "1.1.0"
    match = Mock()
    match.group.side_effect = ["1.0", None]
    ps_module_dep_finder._parse_version_match(match, 'ps_version')
    assert ps_module_dep_finder.ps_version == "1.1.0"

def test_parse_version_match_no_existing_version(ps_module_dep_finder):
    match = Mock()
    match.group.side_effect = ["1.0", "minor"]
    ps_module_dep_finder._parse_version_match(match, 'ps_version')
    assert ps_module_dep_finder.ps_version == "1.0"
