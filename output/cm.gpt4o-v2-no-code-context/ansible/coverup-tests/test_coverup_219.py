# file: lib/ansible/executor/powershell/module_manifest.py:237-251
# asked: {"lines": [237, 238, 242, 243, 245, 246, 247, 250, 251], "branches": [[242, 243], [242, 245], [246, 247], [246, 250], [250, 0], [250, 251]]}
# gained: {"lines": [237, 238, 242, 243, 245, 246, 247, 250, 251], "branches": [[242, 243], [242, 245], [246, 247], [246, 250], [250, 0], [250, 251]]}

import pytest
from ansible.executor.powershell.module_manifest import PSModuleDepFinder
from ansible.module_utils._text import to_text
from distutils.version import LooseVersion

@pytest.fixture
def ps_module_dep_finder():
    return PSModuleDepFinder()

def test_parse_version_match_no_minor_version(ps_module_dep_finder):
    class MockMatch:
        def group(self, index):
            if index == 1:
                return "1"
            if index == 2:
                return None

    ps_module_dep_finder._parse_version_match(MockMatch(), 'version')
    assert ps_module_dep_finder.version == "1.0"

def test_parse_version_match_with_minor_version(ps_module_dep_finder):
    class MockMatch:
        def group(self, index):
            if index == 1:
                return "1.2"
            if index == 2:
                return "2"

    ps_module_dep_finder._parse_version_match(MockMatch(), 'version')
    assert ps_module_dep_finder.version == "1.2"

def test_parse_version_match_existing_version_none(ps_module_dep_finder):
    class MockMatch:
        def group(self, index):
            if index == 1:
                return "1.2"
            if index == 2:
                return "2"

    ps_module_dep_finder._parse_version_match(MockMatch(), 'version')
    assert ps_module_dep_finder.version == "1.2"

def test_parse_version_match_existing_version_newer(ps_module_dep_finder):
    class MockMatch:
        def group(self, index):
            if index == 1:
                return "1.2"
            if index == 2:
                return "2"

    ps_module_dep_finder.version = "1.1"
    ps_module_dep_finder._parse_version_match(MockMatch(), 'version')
    assert ps_module_dep_finder.version == "1.2"

def test_parse_version_match_existing_version_older(ps_module_dep_finder):
    class MockMatch:
        def group(self, index):
            if index == 1:
                return "1.0"
            if index == 2:
                return "0"

    ps_module_dep_finder.version = "1.1"
    ps_module_dep_finder._parse_version_match(MockMatch(), 'version')
    assert ps_module_dep_finder.version == "1.1"
