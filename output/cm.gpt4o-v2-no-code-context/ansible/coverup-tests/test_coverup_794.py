# file: lib/ansible/utils/version.py:265-266
# asked: {"lines": [265, 266], "branches": []}
# gained: {"lines": [265, 266], "branches": []}

import pytest
from ansible.utils.version import SemanticVersion

def test_semantic_version_le(monkeypatch):
    class MockVersion:
        def _cmp(self, other):
            return -1  # Simulate self being less than other

    mock_version = MockVersion()
    sem_ver = SemanticVersion("1.0.0")

    monkeypatch.setattr(sem_ver, '_cmp', mock_version._cmp)
    
    other_version = SemanticVersion("2.0.0")
    assert sem_ver <= other_version

    monkeypatch.undo()

    class MockVersionEqual:
        def _cmp(self, other):
            return 0  # Simulate self being equal to other

    mock_version_equal = MockVersionEqual()
    sem_ver_equal = SemanticVersion("1.0.0")

    monkeypatch.setattr(sem_ver_equal, '_cmp', mock_version_equal._cmp)
    
    other_version_equal = SemanticVersion("1.0.0")
    assert sem_ver_equal <= other_version_equal

    monkeypatch.undo()

    class MockVersionGreater:
        def _cmp(self, other):
            return 1  # Simulate self being greater than other

    mock_version_greater = MockVersionGreater()
    sem_ver_greater = SemanticVersion("2.0.0")

    monkeypatch.setattr(sem_ver_greater, '_cmp', mock_version_greater._cmp)
    
    other_version_greater = SemanticVersion("1.0.0")
    assert not (sem_ver_greater <= other_version_greater)

    monkeypatch.undo()
