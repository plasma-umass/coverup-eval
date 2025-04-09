# file: lib/ansible/utils/version.py:214-219
# asked: {"lines": [214, 215, 219], "branches": []}
# gained: {"lines": [214, 215, 219], "branches": []}

import pytest
from ansible.utils.version import SemanticVersion

def test_is_stable_with_major_zero():
    version = SemanticVersion("0.1.0")
    assert not version.is_stable

def test_is_stable_with_prerelease():
    version = SemanticVersion("1.0.0-alpha")
    assert not version.is_stable

def test_is_stable_with_stable_version():
    version = SemanticVersion("1.0.0")
    assert version.is_stable

def test_is_stable_with_major_zero_and_prerelease():
    version = SemanticVersion("0.1.0-alpha")
    assert not version.is_stable
