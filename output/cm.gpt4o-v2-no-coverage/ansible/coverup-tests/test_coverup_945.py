# file: lib/ansible/utils/version.py:265-266
# asked: {"lines": [265, 266], "branches": []}
# gained: {"lines": [265, 266], "branches": []}

import pytest
from ansible.utils.version import SemanticVersion

def test_semantic_version_le():
    version1 = SemanticVersion("1.0.0")
    version2 = SemanticVersion("2.0.0")
    version3 = SemanticVersion("1.0.0")

    assert version1 <= version2
    assert version1 <= version3
    assert not (version2 <= version1)

    # Clean up
    del version1
    del version2
    del version3
