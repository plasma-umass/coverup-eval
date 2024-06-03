# file lib/ansible/utils/version.py:271-272
# lines [271, 272]
# branches []

import pytest
from ansible.utils.version import SemanticVersion
from packaging.version import Version

def test_semantic_version_ge():
    version1 = SemanticVersion("1.0.0")
    version2 = SemanticVersion("1.0.1")
    version3 = SemanticVersion("1.0.0")

    assert version2 >= version1  # version2 is greater than version1
    assert version1 >= version3  # version1 is equal to version3
    assert not (version1 >= version2)  # version1 is not greater than version2

