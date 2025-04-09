# file lib/ansible/module_utils/compat/version.py:327-328
# lines [327, 328]
# branches []

import pytest
from ansible.module_utils.compat.version import LooseVersion

def test_loose_version_repr():
    version_string = "1.0.0"
    loose_version = LooseVersion(version_string)
    expected_repr = "LooseVersion ('1.0.0')"
    assert repr(loose_version) == expected_repr
