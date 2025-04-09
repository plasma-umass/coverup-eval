# file lib/ansible/module_utils/compat/version.py:158-167
# lines [158, 159, 160, 162, 164, 165, 167]
# branches ['159->160', '159->162', '164->165', '164->167']

import pytest
from ansible.module_utils.compat.version import StrictVersion

def test_strict_version_str():
    # Test case where version[2] == 0
    version = StrictVersion('1.2.0')
    assert str(version) == '1.2'

    # Test case where version[2] != 0
    version = StrictVersion('1.2.3')
    assert str(version) == '1.2.3'

    # Test case with prerelease
    version = StrictVersion('1.2.3a1')
    assert str(version) == '1.2.3a1'

    # Test case with version[2] == 0 and prerelease
    version = StrictVersion('1.2.0a1')
    assert str(version) == '1.2a1'
