# file: lib/ansible/module_utils/compat/version.py:324-325
# asked: {"lines": [324, 325], "branches": []}
# gained: {"lines": [324, 325], "branches": []}

import pytest
from ansible.module_utils.compat.version import LooseVersion

def test_loose_version_str():
    version_string = "1.0.0"
    lv = LooseVersion(version_string)
    assert str(lv) == version_string
