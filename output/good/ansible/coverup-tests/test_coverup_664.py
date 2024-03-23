# file lib/ansible/module_utils/compat/version.py:306-308
# lines [306, 307, 308]
# branches ['307->exit', '307->308']

import pytest
from ansible.module_utils.compat.version import LooseVersion

def test_loose_version_init_with_vstring():
    # Test initialization with a version string
    version_string = "1.0.0"
    version = LooseVersion(version_string)
    assert version.vstring == version_string

def test_loose_version_init_without_vstring(mocker):
    # Test initialization without a version string
    mocker.patch.object(LooseVersion, 'parse')
    version = LooseVersion()
    LooseVersion.parse.assert_not_called()
