# file thefuck/conf.py:115-127
# lines [115, 117, 118, 120, 121, 122, 123, 124, 125, 126, 127]
# branches ['117->118', '117->120', '121->122', '121->123', '123->124', '123->125', '125->126', '125->127']

import pytest
from thefuck.conf import Settings

class Args:
    yes = None
    debug = None
    repeat = None

@pytest.fixture
def mock_args(mocker):
    return mocker.Mock(spec=Args)

def test_settings_from_args_yes(mock_args):
    mock_args.yes = True
    settings = Settings()
    from_args = settings._settings_from_args(mock_args)
    assert from_args['require_confirmation'] is False

def test_settings_from_args_debug(mock_args):
    mock_args.debug = True
    settings = Settings()
    from_args = settings._settings_from_args(mock_args)
    assert from_args['debug'] is True

def test_settings_from_args_repeat(mock_args):
    mock_args.repeat = 5
    settings = Settings()
    from_args = settings._settings_from_args(mock_args)
    assert from_args['repeat'] == 5

def test_settings_from_args_empty(mock_args):
    mock_args.yes = False
    mock_args.debug = False
    mock_args.repeat = 0
    settings = Settings()
    from_args = settings._settings_from_args(mock_args)
    assert from_args == {}
