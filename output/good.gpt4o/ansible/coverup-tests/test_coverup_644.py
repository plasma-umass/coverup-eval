# file lib/ansible/module_utils/compat/version.py:306-308
# lines [306, 307, 308]
# branches ['307->exit', '307->308']

import pytest
from ansible.module_utils.compat.version import LooseVersion

def test_loose_version_init_with_vstring():
    version_string = "1.2.3"
    lv = LooseVersion(version_string)
    assert lv.vstring == version_string

def test_loose_version_init_without_vstring():
    lv = LooseVersion()
    assert not hasattr(lv, 'vstring')
