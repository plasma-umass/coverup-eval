# file mimesis/providers/path.py:85-96
# lines [93, 94, 95, 96]
# branches []

import pytest
from mimesis.providers import Path
from unittest.mock import patch

@pytest.fixture
def path_provider():
    return Path()

def test_dev_dir(path_provider):
    with patch.object(path_provider, 'user') as mock_user, \
         patch.object(path_provider.random, 'choice') as mock_choice:
        mock_user.return_value = 'testuser'
        mock_choice.side_effect = lambda x: x[0]  # Always choose the first option

        result = path_provider.dev_dir()

        # Verify that the result is constructed correctly
        assert result.startswith('/home/testuser/Development/')
        # Since we don't have access to PROGRAMMING_LANGS, we can't assert the exact language
        # Instead, we check that the last part of the path is not 'Development' or 'Dev'
        assert result.split('/')[-1] not in ['Development', 'Dev']

        # Verify that the mocks were called
        mock_user.assert_called_once()
        assert mock_choice.call_count == 2
