# file: lib/ansible/utils/version.py:265-266
# asked: {"lines": [265, 266], "branches": []}
# gained: {"lines": [265, 266], "branches": []}

import pytest
from ansible.module_utils.compat.version import Version
from ansible.utils.version import SemanticVersion

def test_semantic_version_le():
    v1 = SemanticVersion("1.0.0")
    v2 = SemanticVersion("2.0.0")
    
    assert v1 <= v2
    assert not (v2 <= v1)

    v3 = SemanticVersion("1.0.0")
    assert v1 <= v3
    assert v3 <= v1

    v4 = SemanticVersion("1.0.1")
    assert v1 <= v4
    assert not (v4 <= v1)
