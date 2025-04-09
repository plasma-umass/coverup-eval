# file: lib/ansible/module_utils/facts/collector.py:78-82
# asked: {"lines": [78, 79, 80, 81, 82], "branches": [[80, 81], [80, 82]]}
# gained: {"lines": [78, 79, 80, 81, 82], "branches": [[80, 81], [80, 82]]}

import pytest
from ansible.module_utils.facts.collector import BaseFactCollector

class TestBaseFactCollector:
    
    @pytest.fixture(autouse=True)
    def setup(self, monkeypatch):
        # Setup any state or monkeypatching here if necessary
        self.collector = BaseFactCollector()
        yield
        # Teardown any state or monkeypatching here if necessary

    def test_platform_match_system_matches(self):
        platform_info = {'system': 'Generic'}
        result = BaseFactCollector.platform_match(platform_info)
        assert result == BaseFactCollector

    def test_platform_match_system_does_not_match(self):
        platform_info = {'system': 'NonGeneric'}
        result = BaseFactCollector.platform_match(platform_info)
        assert result is None
