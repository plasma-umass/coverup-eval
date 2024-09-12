# file: lib/ansible/module_utils/compat/version.py:306-308
# asked: {"lines": [], "branches": [[307, 0]]}
# gained: {"lines": [], "branches": [[307, 0]]}

import pytest
from ansible.module_utils.compat.version import LooseVersion

def test_looseversion_init_with_vstring():
    version_string = "1.2.3"
    lv = LooseVersion(version_string)
    assert lv.vstring == version_string
    assert lv.version == [1, 2, 3]

def test_looseversion_init_without_vstring():
    lv = LooseVersion()
    assert not hasattr(lv, 'vstring')
    assert not hasattr(lv, 'version')
