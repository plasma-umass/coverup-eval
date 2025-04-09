# file: lib/ansible/utils/version.py:271-272
# asked: {"lines": [271, 272], "branches": []}
# gained: {"lines": [271, 272], "branches": []}

import pytest
from ansible.utils.version import SemanticVersion

def test_semantic_version_ge(monkeypatch):
    class MockVersion:
        def _cmp(self, other):
            return 1

    mock_version = MockVersion()
    sem_ver = SemanticVersion("1.0.0")

    monkeypatch.setattr(sem_ver, '_cmp', mock_version._cmp)
    
    other_version = SemanticVersion("0.9.0")
    assert sem_ver >= other_version

    monkeypatch.undo()
