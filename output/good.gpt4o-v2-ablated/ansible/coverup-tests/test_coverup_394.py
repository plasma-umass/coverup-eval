# file: lib/ansible/module_utils/compat/version.py:324-325
# asked: {"lines": [324, 325], "branches": []}
# gained: {"lines": [324, 325], "branches": []}

import pytest
from ansible.module_utils.compat.version import LooseVersion

class TestLooseVersion:
    def test_str_method(self):
        version_string = "1.0.0"
        version = LooseVersion(version_string)
        assert str(version) == version_string
