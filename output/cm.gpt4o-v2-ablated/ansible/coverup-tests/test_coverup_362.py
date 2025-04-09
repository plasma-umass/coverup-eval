# file: lib/ansible/utils/version.py:271-272
# asked: {"lines": [271, 272], "branches": []}
# gained: {"lines": [271, 272], "branches": []}

import pytest
from ansible.utils.version import SemanticVersion

class TestSemanticVersion:
    def test_ge_true(self):
        version1 = SemanticVersion("1.0.0")
        version2 = SemanticVersion("0.9.0")
        assert version1 >= version2

    def test_ge_false(self):
        version1 = SemanticVersion("1.0.0")
        version2 = SemanticVersion("1.1.0")
        assert not (version1 >= version2)

    def test_ge_equal(self):
        version1 = SemanticVersion("1.0.0")
        version2 = SemanticVersion("1.0.0")
        assert version1 >= version2
