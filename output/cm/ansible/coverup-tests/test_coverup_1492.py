# file lib/ansible/utils/version.py:271-272
# lines [272]
# branches []

import pytest
from ansible.utils.version import SemanticVersion

def test_semantic_version_greater_equal():
    v1 = SemanticVersion('2.0.0')
    v2 = SemanticVersion('1.9.9')
    v3 = SemanticVersion('2.0.0')
    v4 = SemanticVersion('2.0.1')

    assert v1 >= v2, "v1 should be greater than or equal to v2"
    assert v1 >= v3, "v1 should be equal to v3"
    assert not (v1 >= v4), "v1 should not be greater than v4"
