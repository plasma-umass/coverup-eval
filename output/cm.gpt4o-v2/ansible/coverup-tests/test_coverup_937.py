# file: lib/ansible/utils/version.py:271-272
# asked: {"lines": [271, 272], "branches": []}
# gained: {"lines": [271, 272], "branches": []}

import pytest
from ansible.utils.version import SemanticVersion

def test_semantic_version_ge():
    version1 = SemanticVersion("1.0.0")
    version2 = SemanticVersion("2.0.0")
    version3 = SemanticVersion("1.0.0")

    assert version2 >= version1  # Should be True
    assert version1 >= version3  # Should be True
    assert not (version1 >= version2)  # Should be False
