# file: lib/ansible/utils/version.py:271-272
# asked: {"lines": [271, 272], "branches": []}
# gained: {"lines": [271, 272], "branches": []}

import pytest
from ansible.utils.version import SemanticVersion

def test_semantic_version_ge():
    version1 = SemanticVersion("1.0.0")
    version2 = SemanticVersion("1.0.0")
    version3 = SemanticVersion("2.0.0")

    assert version1 >= version2  # should be True, same version
    assert not (version1 >= version3)  # should be False, version1 is less than version3
    assert version3 >= version1  # should be True, version3 is greater than version1
