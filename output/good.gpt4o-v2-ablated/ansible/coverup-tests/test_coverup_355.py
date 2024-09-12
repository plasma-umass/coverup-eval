# file: lib/ansible/utils/version.py:147-148
# asked: {"lines": [147, 148], "branches": []}
# gained: {"lines": [147, 148], "branches": []}

import pytest
from ansible.utils.version import SemanticVersion

def test_semantic_version_repr():
    version_string = "1.0.0"
    sem_ver = SemanticVersion(version_string)
    assert repr(sem_ver) == f"SemanticVersion('{version_string}')"
