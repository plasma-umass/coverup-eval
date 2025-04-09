# file mimesis/providers/path.py:85-96
# lines [93, 94, 95, 96]
# branches []

import pytest
from mimesis import Generic
from mimesis.providers.path import Path
from unittest.mock import patch

@pytest.fixture
def path_provider():
    return Path()

def test_dev_dir(path_provider, mocker):
    mock_user = mocker.patch.object(path_provider, 'user', return_value='testuser')
    mock_choice = mocker.patch.object(path_provider.random, 'choice', side_effect=['Development', 'Python'])
    
    # Mock the PROGRAMMING_LANGS constant
    mock_programming_langs = mocker.patch('mimesis.providers.path.PROGRAMMING_LANGS', ['Python', 'Java', 'C++'])

    result = path_provider.dev_dir()

    assert result == str(path_provider._pathlib_home / 'testuser' / 'Development' / 'Python')
    mock_user.assert_called_once()
    assert mock_choice.call_count == 2
    mock_choice.assert_any_call(['Development', 'Dev'])
    mock_choice.assert_any_call(mock_programming_langs)
