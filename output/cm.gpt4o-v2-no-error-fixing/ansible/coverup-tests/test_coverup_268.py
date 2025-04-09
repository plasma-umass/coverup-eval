# file: lib/ansible/module_utils/compat/version.py:158-167
# asked: {"lines": [158, 159, 160, 162, 164, 165, 167], "branches": [[159, 160], [159, 162], [164, 165], [164, 167]]}
# gained: {"lines": [158, 159, 160, 162, 164, 165, 167], "branches": [[159, 160], [159, 162], [164, 165], [164, 167]]}

import pytest
from ansible.module_utils.compat.version import StrictVersion

def test_strict_version_str():
    # Test case where version has two components and no prerelease
    version = StrictVersion("1.2")
    assert str(version) == "1.2"

    # Test case where version has three components and no prerelease
    version = StrictVersion("1.2.3")
    assert str(version) == "1.2.3"

    # Test case where version has a prerelease
    version = StrictVersion("1.2.3a1")
    assert str(version) == "1.2.3a1"

    # Test case where version has two components and a prerelease
    version = StrictVersion("1.2a1")
    assert str(version) == "1.2a1"
