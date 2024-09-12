# file: lib/ansible/utils/version.py:268-269
# asked: {"lines": [268, 269], "branches": []}
# gained: {"lines": [268, 269], "branches": []}

import pytest
from ansible.utils.version import SemanticVersion

class TestSemanticVersion:
    def test_gt_true(self):
        version1 = SemanticVersion("2.0.0")
        version2 = SemanticVersion("1.0.0")
        assert version1 > version2

    def test_gt_false(self):
        version1 = SemanticVersion("1.0.0")
        version2 = SemanticVersion("2.0.0")
        assert not (version1 > version2)

    def test_gt_equal(self):
        version1 = SemanticVersion("1.0.0")
        version2 = SemanticVersion("1.0.0")
        assert not (version1 > version2)
