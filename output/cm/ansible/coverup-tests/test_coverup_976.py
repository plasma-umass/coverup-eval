# file lib/ansible/utils/version.py:265-266
# lines [265, 266]
# branches []

import pytest
from ansible.utils.version import SemanticVersion

def test_semantic_version_le_operator():
    v1 = SemanticVersion('2.0.0')
    v2 = SemanticVersion('2.0.1')
    v3 = SemanticVersion('2.0.0')
    
    assert (v1 <= v2) == True, "v1 should be less than or equal to v2"
    assert (v2 <= v1) == False, "v2 should not be less than v1"
    assert (v1 <= v3) == True, "v1 should be equal to v3"
