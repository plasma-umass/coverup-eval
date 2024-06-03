# file mimesis/providers/text.py:113-122
# lines [113, 121, 122]
# branches []

import pytest
from mimesis.providers.text import Text
from mimesis import Generic

@pytest.fixture
def text_provider():
    generic = Generic()
    return generic.text

def test_quote(text_provider, mocker):
    mock_data = {'quotes': ["Bond... James Bond.", "May the Force be with you.", "I'll be back."]}
    mocker.patch.object(text_provider, '_data', mock_data)
    
    quote = text_provider.quote()
    
    assert quote in mock_data['quotes']
