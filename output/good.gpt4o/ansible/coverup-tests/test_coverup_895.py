# file lib/ansible/utils/version.py:268-269
# lines [268, 269]
# branches []

import pytest
from ansible.utils.version import SemanticVersion

def test_semantic_version_gt():
    version1 = SemanticVersion("1.0.0")
    version2 = SemanticVersion("2.0.0")
    version3 = SemanticVersion("1.0.0")

    assert version2 > version1, "Expected version2 to be greater than version1"
    assert not (version1 > version2), "Expected version1 to not be greater than version2"
    assert not (version1 > version3), "Expected version1 to not be greater than version3"
