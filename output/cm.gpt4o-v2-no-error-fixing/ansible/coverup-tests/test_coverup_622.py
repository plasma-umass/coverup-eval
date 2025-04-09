# file: lib/ansible/utils/version.py:256-257
# asked: {"lines": [256, 257], "branches": []}
# gained: {"lines": [256, 257], "branches": []}

import pytest
from ansible.utils.version import SemanticVersion

def test_semantic_version_eq():
    version1 = SemanticVersion("1.0.0")
    version2 = SemanticVersion("1.0.0")
    version3 = SemanticVersion("2.0.0")

    assert version1 == version2  # This should trigger the __eq__ method and return True
    assert not (version1 == version3)  # This should trigger the __eq__ method and return False
