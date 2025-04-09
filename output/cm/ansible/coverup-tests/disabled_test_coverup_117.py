# file lib/ansible/plugins/connection/psrp.py:468-497
# lines [468, 469, 471, 472, 477, 478, 481, 482, 483, 485, 486, 488, 489, 491, 492, 493, 495, 496, 497]
# branches ['477->478', '477->481', '485->486', '485->488', '491->492', '491->495', '495->exit', '495->496']

import json
import pytest
from ansible.errors import AnsibleError
from ansible.plugins.connection.psrp import Connection
from ansible.playbook.play_context import PlayContext
from ansible.utils.display import Display
from unittest.mock import MagicMock

# Mock the global variable NEWER_PYPSRP
NEWER_PYPSRP = False

# Mock the Display class to prevent actual output during tests
@pytest.fixture
def mock_display(mocker):
    mocker.patch.object(Display, 'vvv')
    mocker.patch.object(Display, 'deprecated')

# Mock the ConnectionBase class to prevent actual file operations
@pytest.fixture
def mock_connection_base(mocker):
    mocker.patch('ansible.plugins.connection.psrp.ConnectionBase.put_file')

# Mock the _put_file_old method to simulate the file transfer
@pytest.fixture
def mock_put_file_old(mocker):
    def put_file_old(self, in_path, out_path):
        return 0, json.dumps({"sha1": "dummy_sha1"}), "", "dummy_sha1"
    mocker.patch('ansible.plugins.connection.psrp.Connection._put_file_old', new=put_file_old)

# Test function to improve coverage
def test_put_file_with_older_pypsrp(mock_display, mock_connection_base, mock_put_file_old, mocker):
    play_context = PlayContext()
    play_context.shell = 'powershell'
    connection = Connection(play_context, MagicMock(), MagicMock())
    connection._psrp_host = 'dummy_host'
    connection._shell = mocker.Mock()
    connection._shell._unquote = lambda x: x

    # Test with successful file transfer
    try:
        connection.put_file('dummy_in_path', 'dummy_out_path')
    except AnsibleError:
        pytest.fail("Unexpected AnsibleError raised")

    # Test with failed file transfer (non-zero return code)
    with pytest.raises(AnsibleError):
        with mocker.patch('ansible.plugins.connection.psrp.Connection._put_file_old', return_value=(1, "", "error", "")):
            connection.put_file('dummy_in_path', 'dummy_out_path')

    # Test with missing remote sha1
    with pytest.raises(AnsibleError):
        with mocker.patch('ansible.plugins.connection.psrp.Connection._put_file_old', return_value=(0, json.dumps({}), "", "dummy_sha1")):
            connection.put_file('dummy_in_path', 'dummy_out_path')

    # Test with mismatching sha1
    with pytest.raises(AnsibleError):
        with mocker.patch('ansible.plugins.connection.psrp.Connection._put_file_old', return_value=(0, json.dumps({"sha1": "wrong_sha1"}), "", "dummy_sha1")):
            connection.put_file('dummy_in_path', 'dummy_out_path')
