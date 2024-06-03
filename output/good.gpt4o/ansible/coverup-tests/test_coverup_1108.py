# file lib/ansible/executor/powershell/module_manifest.py:237-251
# lines [238, 242, 243, 245, 246, 247, 250, 251]
# branches ['242->243', '242->245', '246->247', '246->250', '250->exit', '250->251']

import pytest
from unittest.mock import Mock, patch
from ansible.executor.powershell.module_manifest import PSModuleDepFinder
from distutils.version import LooseVersion

@pytest.fixture
def ps_module_dep_finder():
    return PSModuleDepFinder()

def test_parse_version_match(ps_module_dep_finder):
    match = Mock()
    match.group.side_effect = ["1", None]
    attribute = "version"

    ps_module_dep_finder._parse_version_match(match, attribute)
    assert getattr(ps_module_dep_finder, attribute) == "1.0"

    match.group.side_effect = ["2.1", "0"]
    ps_module_dep_finder._parse_version_match(match, attribute)
    assert getattr(ps_module_dep_finder, attribute) == "2.1"

    match.group.side_effect = ["1.5", "0"]
    ps_module_dep_finder._parse_version_match(match, attribute)
    assert getattr(ps_module_dep_finder, attribute) == "2.1"

    match.group.side_effect = ["3.0", "0"]
    ps_module_dep_finder._parse_version_match(match, attribute)
    assert getattr(ps_module_dep_finder, attribute) == "3.0"
