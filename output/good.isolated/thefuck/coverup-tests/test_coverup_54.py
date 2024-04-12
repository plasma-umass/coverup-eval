# file thefuck/logs.py:20-25
# lines [20, 21, 22, 23, 24, 25]
# branches []

import sys
from thefuck.logs import warn
import colorama
from pytest import fixture
from io import StringIO

@fixture
def mock_stderr(mocker):
    mocker.patch('sys.stderr', new_callable=StringIO)

def test_warn(mocker):
    mock_stderr = StringIO()
    mocker.patch('sys.stderr', new=mock_stderr)
    
    expected_output = u'{warn}[WARN] Test Warning{reset}\n'.format(
        warn=colorama.Back.RED + colorama.Fore.WHITE + colorama.Style.BRIGHT,
        reset=colorama.Style.RESET_ALL,
        title="Test Warning"
    )
    
    warn("Test Warning")
    
    assert mock_stderr.getvalue() == expected_output
