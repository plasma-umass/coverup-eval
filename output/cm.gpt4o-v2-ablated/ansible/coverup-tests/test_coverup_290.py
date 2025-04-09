# file: lib/ansible/utils/version.py:206-208
# asked: {"lines": [206, 207, 208], "branches": []}
# gained: {"lines": [206, 207, 208], "branches": []}

import pytest
from ansible.utils.version import SemanticVersion

class TestSemanticVersion:
    @pytest.fixture
    def version(self):
        return SemanticVersion("1.2.3")

    def test_core(self, version):
        assert version.core == (1, 2, 3)
