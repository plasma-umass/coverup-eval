# file lib/ansible/utils/version.py:262-263
# lines [262, 263]
# branches []

import pytest
from ansible.utils.version import SemanticVersion
from packaging.version import Version

def test_semantic_version_lt():
    version1 = SemanticVersion("1.0.0")
    version2 = SemanticVersion("2.0.0")
    version3 = SemanticVersion("1.0.0")

    assert version1 < version2
    assert not (version2 < version1)
    assert not (version1 < version3)

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Add any necessary cleanup code here
