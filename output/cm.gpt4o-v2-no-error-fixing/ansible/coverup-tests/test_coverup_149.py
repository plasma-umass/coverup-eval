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
    match.group.side_effect = ["1", None]
    attribute = "version"

    ps_module_dep_finder._parse_version_match(match, attribute)

    assert getattr(ps_module_dep_finder, attribute) == "1.0"

def test_parse_version_match_existing_version(ps_module_dep_finder):
    match = Mock()
    match.group.side_effect = ["2.1", "1"]
    attribute = "version"
    setattr(ps_module_dep_finder, attribute, "1.0")

    ps_module_dep_finder._parse_version_match(match, attribute)

    assert getattr(ps_module_dep_finder, attribute) == "2.1"

def test_parse_version_match_existing_version_lower(ps_module_dep_finder):
    match = Mock()
    match.group.side_effect = ["1.0", "1"]
    attribute = "version"
    setattr(ps_module_dep_finder, attribute, "2.1")

    ps_module_dep_finder._parse_version_match(match, attribute)

    assert getattr(ps_module_dep_finder, attribute) == "2.1"
