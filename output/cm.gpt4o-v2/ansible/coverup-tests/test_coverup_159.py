# file: lib/ansible/plugins/connection/psrp.py:882-906
# asked: {"lines": [882, 884, 887, 888, 889, 891, 892, 893, 894, 895, 897, 899, 904, 906], "branches": [[884, 887], [884, 891], [893, 894], [893, 897], [894, 895], [894, 897]]}
# gained: {"lines": [882, 884, 887, 888, 889, 891, 892, 893, 894, 895, 897, 899, 904, 906], "branches": [[884, 887], [884, 891], [893, 894], [893, 897], [894, 895], [894, 897]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.connection.psrp import Connection
from ansible.playbook.play_context import PlayContext
from pypsrp.powershell import PowerShell
from pypsrp.complex_objects import PSInvocationState

@pytest.fixture
def connection():
    play_context = PlayContext()
    play_context.shell = 'powershell'
    conn = Connection(play_context, new_stdin=None)
    conn.runspace = MagicMock()
    return conn

def test_exec_psrp_script_no_last_pipeline(connection):
    script = "Write-Output 'Hello World'"
    connection._last_pipeline = None

    with patch.object(PowerShell, 'invoke', return_value=None) as mock_invoke, \
         patch.object(PowerShell, 'add_script') as mock_add_script, \
         patch.object(PowerShell, 'add_argument') as mock_add_argument, \
         patch.object(connection, '_parse_pipeline_result', return_value=(0, 'output', '')) as mock_parse_result:
        
        rc, stdout, stderr = connection._exec_psrp_script(script)

        mock_add_script.assert_called_once_with(script, use_local_scope=True)
        mock_invoke.assert_called_once()
        mock_parse_result.assert_called_once()
        assert rc == 0
        assert stdout == 'output'
        assert stderr == ''
        assert connection._last_pipeline is not None

def test_exec_psrp_script_with_last_pipeline(connection):
    script = "Write-Output 'Hello World'"
    last_pipeline = MagicMock()
    last_pipeline.state = PSInvocationState.COMPLETED
    connection._last_pipeline = last_pipeline

    with patch.object(last_pipeline, 'stop') as mock_stop, \
         patch.object(PowerShell, 'invoke', return_value=None) as mock_invoke, \
         patch.object(PowerShell, 'add_script') as mock_add_script, \
         patch.object(PowerShell, 'add_argument') as mock_add_argument, \
         patch.object(connection, '_parse_pipeline_result', return_value=(0, 'output', '')) as mock_parse_result:
        
        rc, stdout, stderr = connection._exec_psrp_script(script)

        assert last_pipeline.state == PSInvocationState.RUNNING
        mock_stop.assert_called_once()
        mock_add_script.assert_called_once_with(script, use_local_scope=True)
        mock_invoke.assert_called_once()
        mock_parse_result.assert_called_once()
        assert rc == 0
        assert stdout == 'output'
        assert stderr == ''
        assert connection._last_pipeline is not None
        assert connection._last_pipeline != last_pipeline

def test_exec_psrp_script_with_arguments(connection):
    script = "Write-Output 'Hello World'"
    arguments = ['arg1', 'arg2']
    connection._last_pipeline = None

    with patch.object(PowerShell, 'invoke', return_value=None) as mock_invoke, \
         patch.object(PowerShell, 'add_script') as mock_add_script, \
         patch.object(PowerShell, 'add_argument') as mock_add_argument, \
         patch.object(connection, '_parse_pipeline_result', return_value=(0, 'output', '')) as mock_parse_result:
        
        rc, stdout, stderr = connection._exec_psrp_script(script, arguments=arguments)

        mock_add_script.assert_called_once_with(script, use_local_scope=True)
        assert mock_add_argument.call_count == len(arguments)
        mock_invoke.assert_called_once()
        mock_parse_result.assert_called_once()
        assert rc == 0
        assert stdout == 'output'
        assert stderr == ''
        assert connection._last_pipeline is not None
