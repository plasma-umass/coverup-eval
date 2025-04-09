# file: lib/ansible/executor/powershell/module_manifest.py:237-251
# asked: {"lines": [238, 242, 243, 245, 246, 247, 250, 251], "branches": [[242, 243], [242, 245], [246, 247], [246, 250], [250, 0], [250, 251]]}
# gained: {"lines": [238, 242, 243, 245, 246, 247, 250, 251], "branches": [[242, 243], [242, 245], [246, 247], [246, 250], [250, 0], [250, 251]]}

import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.compat.version import LooseVersion
from ansible.module_utils._text import to_text
from ansible.executor.powershell.module_manifest import PSModuleDepFinder

class TestPSModuleDepFinder:
    
    @pytest.fixture
    def ps_module_dep_finder(self):
        return PSModuleDepFinder()
    
    @pytest.fixture
    def match(self):
        mock_match = Mock()
        mock_match.group.side_effect = lambda x: {1: '1.0', 2: None}.get(x)
        return mock_match
    
    def test_parse_version_match_no_existing_version(self, ps_module_dep_finder, match):
        ps_module_dep_finder._parse_version_match(match, 'version')
        assert ps_module_dep_finder.version == '1.0.0'
    
    def test_parse_version_match_with_existing_version(self, ps_module_dep_finder, match):
        ps_module_dep_finder.version = '0.9'
        ps_module_dep_finder._parse_version_match(match, 'version')
        assert ps_module_dep_finder.version == '1.0.0'
    
    def test_parse_version_match_with_higher_existing_version(self, ps_module_dep_finder, match):
        ps_module_dep_finder.version = '1.1'
        ps_module_dep_finder._parse_version_match(match, 'version')
        assert ps_module_dep_finder.version == '1.1'
    
    def test_parse_version_match_with_non_none_group2(self, ps_module_dep_finder, match):
        match.group.side_effect = lambda x: {1: '1.0', 2: '1'}.get(x)
        ps_module_dep_finder._parse_version_match(match, 'version')
        assert ps_module_dep_finder.version == '1.0'
