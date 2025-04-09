# file thefuck/entrypoints/alias.py:7-22
# lines [16]
# branches ['15->16']

import pytest
from thefuck.entrypoints.alias import _get_alias
from thefuck.shells import shell
from unittest.mock import patch
import six


@pytest.fixture
def mock_shell(mocker):
    mocker.patch.object(shell, 'app_alias', return_value='alias')
    mocker.patch.object(shell, 'instant_mode_alias', return_value='instant_alias')


@pytest.fixture
def mock_warn(mocker):
    return mocker.patch('thefuck.entrypoints.alias.warn')


def test_get_alias_with_experimental_instant_mode_on_py2(mock_shell, mock_warn):
    known_args = type('argparse', (object,), {'enable_experimental_instant_mode': True, 'alias': 'fuck'})
    with patch.object(six, 'PY2', True):
        result = _get_alias(known_args)
        mock_warn.assert_called_with("Instant mode requires Python 3")
        assert result == 'alias'
