# file lib/ansible/module_utils/compat/selinux.py:101-107
# lines [102, 103, 104, 105, 107]
# branches []

import pytest
from ctypes import c_char_p, byref
from ansible.module_utils.compat import selinux

# Mock the _selinux_lib object within the selinux module
@pytest.fixture
def mock_selinux_lib(mocker):
    mock_lib = mocker.MagicMock()
    mocker.patch.object(selinux, '_selinux_lib', mock_lib)
    return mock_lib

# Test function to cover lines 102-107
def test_matchpathcon(mock_selinux_lib):
    # Setup the mock for matchpathcon and freecon
    mock_selinux_lib.matchpathcon.return_value = 0
    mock_selinux_lib.freecon.return_value = None

    # Call the function with a dummy path and mode
    rc, con_value = selinux.matchpathcon('/dummy/path', 0)

    # Assertions to check the return value and that freecon was called
    assert rc == 0
    assert con_value is not None
    mock_selinux_lib.freecon.assert_called_once()

    # Cleanup is handled by the fixture and mock library
