# file mimesis/providers/path.py:98-108
# lines [106, 107, 108]
# branches []

import pytest
from mimesis.providers import Path
from unittest.mock import patch

# Assuming PROJECT_NAMES is a constant list in the same module
from mimesis.providers.path import PROJECT_NAMES

@pytest.fixture
def path_provider():
    return Path()

def test_project_dir(path_provider):
    with patch.object(path_provider, 'dev_dir') as mock_dev_dir, \
         patch.object(path_provider.random, 'choice') as mock_choice:
        mock_dev_dir.return_value = 'Development'
        mock_choice.return_value = 'Falcon'
        
        result = path_provider.project_dir()
        
        mock_dev_dir.assert_called_once()
        mock_choice.assert_called_once_with(PROJECT_NAMES)
        assert 'Development/Falcon' in result
