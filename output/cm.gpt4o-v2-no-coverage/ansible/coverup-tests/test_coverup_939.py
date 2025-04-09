# file: lib/ansible/utils/version.py:259-260
# asked: {"lines": [259, 260], "branches": []}
# gained: {"lines": [259, 260], "branches": []}

import pytest
from ansible.utils.version import SemanticVersion

def test_semantic_version_ne():
    v1 = SemanticVersion("1.0.0")
    v2 = SemanticVersion("1.0.1")
    v3 = SemanticVersion("1.0.0")

    assert v1 != v2  # Different versions should not be equal
    assert not (v1 != v3)  # Same versions should be equal

    # Clean up
    del v1
    del v2
    del v3
