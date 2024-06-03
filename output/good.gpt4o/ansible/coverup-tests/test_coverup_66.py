# file lib/ansible/utils/version.py:221-251
# lines [221, 222, 223, 225, 228, 229, 231, 233, 234, 236, 237, 238, 239, 241, 242, 243, 244, 251]
# branches ['222->223', '222->225', '225->228', '225->233', '228->229', '228->231', '233->234', '233->236', '236->237', '236->238', '238->239', '238->241', '241->242', '241->243', '243->244', '243->251']

import pytest
from ansible.utils.version import SemanticVersion

def test_semantic_version_cmp(mocker):
    # Mocking the Version class to avoid dependencies
    mocker.patch('ansible.utils.version.Version', autospec=True)

    # Test cases for different branches
    v1 = SemanticVersion("1.0.0")
    v2 = SemanticVersion("1.0.1")
    v3 = SemanticVersion("1.0.0-alpha")
    v4 = SemanticVersion("1.0.0-beta")
    v5 = SemanticVersion("1.0.0+build")

    # Test core version comparison
    assert v1._cmp(v2) == -1
    assert v2._cmp(v1) == 1

    # Test prerelease comparison
    assert v1._cmp(v3) == 1
    assert v3._cmp(v1) == -1
    assert v3._cmp(v4) == -1
    assert v4._cmp(v3) == 1

    # Test build metadata is ignored
    assert v1._cmp(v5) == 0

    # Test string input
    assert v1._cmp("1.0.1") == -1
    assert v1._cmp("1.0.0-alpha") == 1

    # Test equal versions
    assert v1._cmp(SemanticVersion("1.0.0")) == 0
    assert v3._cmp(SemanticVersion("1.0.0-alpha")) == 0
