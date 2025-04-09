# file: lib/ansible/utils/version.py:210-212
# asked: {"lines": [210, 211, 212], "branches": []}
# gained: {"lines": [210, 211, 212], "branches": []}

import pytest
from ansible.utils.version import SemanticVersion

def test_is_prerelease_true():
    version = SemanticVersion("1.0.0-alpha")
    assert version.is_prerelease is True

def test_is_prerelease_false():
    version = SemanticVersion("1.0.0")
    assert version.is_prerelease is False
