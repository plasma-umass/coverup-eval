# file: lib/ansible/utils/version.py:259-260
# asked: {"lines": [259, 260], "branches": []}
# gained: {"lines": [259, 260], "branches": []}

import pytest
from ansible.utils.version import SemanticVersion

def test_semantic_version_ne():
    v1 = SemanticVersion("1.0.0")
    v2 = SemanticVersion("1.0.1")
    assert v1 != v2  # This should call the __ne__ method and return True

def test_semantic_version_eq():
    v1 = SemanticVersion("1.0.0")
    v2 = SemanticVersion("1.0.0")
    assert v1 == v2  # This should call the __eq__ method and return True
