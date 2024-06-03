# file mimesis/providers/text.py:16-24
# lines [16, 22, 23, 24]
# branches []

import pytest
from mimesis.providers.text import Text

@pytest.fixture
def mock_pull(mocker):
    return mocker.patch('mimesis.providers.text.Text._pull')

def test_text_initialization(mock_pull):
    locale = 'en'
    seed = 1234
    text_provider = Text(locale=locale, seed=seed)
    
    assert text_provider._datafile == 'text.json'
    mock_pull.assert_called_once_with('text.json')
