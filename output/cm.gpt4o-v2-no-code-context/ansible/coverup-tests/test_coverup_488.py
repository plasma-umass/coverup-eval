# file: lib/ansible/module_utils/facts/collector.py:78-82
# asked: {"lines": [78, 79, 80, 81, 82], "branches": [[80, 81], [80, 82]]}
# gained: {"lines": [78, 79, 80, 81, 82], "branches": [[80, 81], [80, 82]]}

import pytest
from ansible.module_utils.facts.collector import BaseFactCollector

class TestBaseFactCollector:
    @pytest.fixture(autouse=True)
    def setup(self, monkeypatch):
        # Setup a mock platform for testing
        self.mock_platform = 'Linux'
        monkeypatch.setattr(BaseFactCollector, '_platform', self.mock_platform)

    def test_platform_match_success(self):
        platform_info = {'system': 'Linux'}
        result = BaseFactCollector.platform_match(platform_info)
        assert result == BaseFactCollector

    def test_platform_match_failure(self):
        platform_info = {'system': 'Windows'}
        result = BaseFactCollector.platform_match(platform_info)
        assert result is None
