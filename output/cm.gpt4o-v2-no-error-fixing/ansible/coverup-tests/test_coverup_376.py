# file: lib/ansible/module_utils/facts/collector.py:78-82
# asked: {"lines": [78, 79, 80, 81, 82], "branches": [[80, 81], [80, 82]]}
# gained: {"lines": [78, 79, 80, 81, 82], "branches": [[80, 81], [80, 82]]}

import pytest
from ansible.module_utils.facts.collector import BaseFactCollector

class TestBaseFactCollector:
    
    @pytest.fixture
    def platform_info_generic(self):
        return {'system': 'Generic'}
    
    @pytest.fixture
    def platform_info_other(self):
        return {'system': 'Other'}
    
    def test_platform_match_generic(self, platform_info_generic):
        assert BaseFactCollector.platform_match(platform_info_generic) == BaseFactCollector
    
    def test_platform_match_other(self, platform_info_other):
        assert BaseFactCollector.platform_match(platform_info_other) is None
