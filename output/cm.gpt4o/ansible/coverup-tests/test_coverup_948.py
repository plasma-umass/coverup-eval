# file lib/ansible/module_utils/compat/version.py:324-325
# lines [324, 325]
# branches []

import pytest
from ansible.module_utils.compat.version import LooseVersion

def test_loose_version_str():
    version_string = "1.0.0"
    loose_version = LooseVersion(version_string)
    assert str(loose_version) == version_string
