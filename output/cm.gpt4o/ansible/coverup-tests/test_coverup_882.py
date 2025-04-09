# file lib/ansible/utils/version.py:256-257
# lines [256, 257]
# branches []

import pytest
from ansible.utils.version import SemanticVersion
from packaging.version import Version

def test_semantic_version_eq():
    version1 = SemanticVersion("1.0.0")
    version2 = SemanticVersion("1.0.0")
    version3 = SemanticVersion("2.0.0")

    assert version1 == version2, "Versions should be equal"
    assert version1 != version3, "Versions should not be equal"
