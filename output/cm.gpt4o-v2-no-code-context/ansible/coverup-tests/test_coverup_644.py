# file: lib/ansible/utils/version.py:206-208
# asked: {"lines": [206, 207, 208], "branches": []}
# gained: {"lines": [206, 207, 208], "branches": []}

import pytest
from ansible.utils.version import SemanticVersion

def test_semantic_version_core():
    version = SemanticVersion("1.2.3")
    assert version.core == (1, 2, 3)
