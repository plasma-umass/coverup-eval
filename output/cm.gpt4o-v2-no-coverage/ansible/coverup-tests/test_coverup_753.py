# file: lib/ansible/module_utils/compat/version.py:306-308
# asked: {"lines": [306, 307, 308], "branches": [[307, 0], [307, 308]]}
# gained: {"lines": [306, 307, 308], "branches": [[307, 0], [307, 308]]}

import pytest
from ansible.module_utils.compat.version import LooseVersion

def test_loose_version_init_with_vstring(mocker):
    mocker.patch.object(LooseVersion, 'parse', autospec=True)
    version = LooseVersion("1.2.3")
    version.parse.assert_called_once_with(version, "1.2.3")

def test_loose_version_init_without_vstring(mocker):
    mocker.patch.object(LooseVersion, 'parse', autospec=True)
    version = LooseVersion()
    version.parse.assert_not_called()

def test_loose_version_parse():
    version = LooseVersion()
    version.parse("1.2.3")
    assert version.vstring == "1.2.3"
    assert version.version == [1, 2, 3]

def test_loose_version_parse_with_non_numeric():
    version = LooseVersion()
    version.parse("1.2a.3")
    assert version.vstring == "1.2a.3"
    assert version.version == [1, 2, 'a', 3]
