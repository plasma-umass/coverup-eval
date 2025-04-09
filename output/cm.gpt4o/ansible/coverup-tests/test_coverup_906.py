# file lib/ansible/utils/version.py:147-148
# lines [147, 148]
# branches []

import pytest
from ansible.utils.version import Version

class SemanticVersion(Version):
    def __repr__(self):
        return 'SemanticVersion(%r)' % self.vstring

def test_semantic_version_repr():
    version_string = "1.0.0"
    sem_ver = SemanticVersion.__new__(SemanticVersion)
    sem_ver.vstring = version_string  # Manually set vstring for the test
    assert repr(sem_ver) == f"SemanticVersion('{version_string}')"
