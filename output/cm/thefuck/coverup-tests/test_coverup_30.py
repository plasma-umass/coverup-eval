# file thefuck/shells/generic.py:103-111
# lines [103, 106, 107, 109, 111]
# branches ['106->107', '106->109']

import pytest
from thefuck.shells.generic import Generic
from unittest.mock import patch, MagicMock

@pytest.fixture
def generic_shell():
    return Generic()

def test_quote_py2(generic_shell):
    with patch('thefuck.shells.generic.six.PY2', True):
        with patch('pipes.quote') as mock_quote:
            mock_quote.return_value = 'mocked_value'
            assert generic_shell.quote('test') == 'mocked_value'
            mock_quote.assert_called_once_with('test')

def test_quote_py3(generic_shell):
    with patch('thefuck.shells.generic.six.PY2', False):
        with patch('shlex.quote') as mock_quote:
            mock_quote.return_value = 'mocked_value'
            assert generic_shell.quote('test') == 'mocked_value'
            mock_quote.assert_called_once_with('test')
