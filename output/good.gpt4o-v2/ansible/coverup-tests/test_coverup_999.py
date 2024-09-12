# file: lib/ansible/module_utils/compat/version.py:324-325
# asked: {"lines": [324, 325], "branches": []}
# gained: {"lines": [324, 325], "branches": []}

import pytest
from ansible.module_utils.compat.version import LooseVersion

def test_looseversion_str():
    version_string = "1.5.2b2"
    version = LooseVersion(version_string)
    assert str(version) == version_string
