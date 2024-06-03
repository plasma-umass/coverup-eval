# file thefuck/logs.py:137-141
# lines [137, 138, 139, 140, 141]
# branches []

import sys
import pytest
from unittest import mock
from thefuck.logs import version

def test_version(mocker):
    thefuck_version = "3.30"
    python_version = "3.8.5"
    shell_info = "bash"

    mock_stderr = mocker.patch('sys.stderr', new_callable=mock.Mock)
    mock_stderr.write = mock.Mock()

    version(thefuck_version, python_version, shell_info)

    mock_stderr.write.assert_called_once_with(
        u'The Fuck {} using Python {} and {}\n'.format(thefuck_version, python_version, shell_info)
    )
