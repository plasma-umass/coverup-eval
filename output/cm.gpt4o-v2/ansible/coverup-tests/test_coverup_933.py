# file: lib/ansible/utils/version.py:259-260
# asked: {"lines": [259, 260], "branches": []}
# gained: {"lines": [259, 260], "branches": []}

import pytest
from ansible.utils.version import SemanticVersion

def test_semantic_version_ne():
    version1 = SemanticVersion("1.0.0")
    version2 = SemanticVersion("1.0.1")
    
    assert version1 != version2
    assert not (version1 == version2)
