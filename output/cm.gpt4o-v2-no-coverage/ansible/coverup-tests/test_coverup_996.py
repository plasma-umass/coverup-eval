# file: lib/ansible/module_utils/compat/version.py:324-325
# asked: {"lines": [324, 325], "branches": []}
# gained: {"lines": [324, 325], "branches": []}

import pytest
from ansible.module_utils.compat.version import LooseVersion, Version

class TestLooseVersion:
    def test_str_method(self):
        version_string = "1.0.0"
        lv = LooseVersion(version_string)
        assert str(lv) == version_string

    def test_inheritance(self):
        version_string = "1.0.0"
        lv = LooseVersion(version_string)
        assert isinstance(lv, Version)
