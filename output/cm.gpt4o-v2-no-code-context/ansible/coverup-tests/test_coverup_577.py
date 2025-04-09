# file: lib/ansible/module_utils/compat/version.py:306-308
# asked: {"lines": [306, 307, 308], "branches": [[307, 0], [307, 308]]}
# gained: {"lines": [306, 307, 308], "branches": [[307, 0], [307, 308]]}

import pytest
from ansible.module_utils.compat.version import LooseVersion

def test_loose_version_init_with_vstring(mocker):
    mock_parse = mocker.patch.object(LooseVersion, 'parse', autospec=True)
    version_string = "1.0.0"
    lv = LooseVersion(version_string)
    mock_parse.assert_called_once_with(lv, version_string)

def test_loose_version_init_without_vstring(mocker):
    mock_parse = mocker.patch.object(LooseVersion, 'parse', autospec=True)
    lv = LooseVersion()
    mock_parse.assert_not_called()
