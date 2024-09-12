# file: lib/ansible/module_utils/compat/version.py:327-328
# asked: {"lines": [327, 328], "branches": []}
# gained: {"lines": [327, 328], "branches": []}

import pytest
from ansible.module_utils.compat.version import LooseVersion

def test_looseversion_repr():
    version = LooseVersion("1.0")
    assert repr(version) == "LooseVersion ('1.0')"
