# file: lib/ansible/utils/version.py:262-263
# asked: {"lines": [262, 263], "branches": []}
# gained: {"lines": [262, 263], "branches": []}

import pytest
from ansible.utils.version import SemanticVersion

def test_semantic_version_lt():
    v1 = SemanticVersion("1.0.0")
    v2 = SemanticVersion("2.0.0")
    assert v1 < v2
    assert not (v2 < v1)
