# file mimesis/providers/text.py:54-63
# lines [54, 60, 61, 62, 63]
# branches ['61->62', '61->63']

import pytest
from mimesis.providers.text import Text

@pytest.fixture
def text_provider():
    return Text()

def test_text_provider_text(mocker, text_provider):
    mock_data = {
        'text': [
            'Lorem ipsum dolor sit amet.',
            'Consectetur adipiscing elit.',
            'Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
            'Ut enim ad minim veniam.',
            'Quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'
        ]
    }
    mocker.patch.object(text_provider, '_data', mock_data)
    mocker.patch.object(text_provider.random, 'choice', side_effect=lambda x: x[0])

    result = text_provider.text(quantity=3)
    assert result == 'Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet.'
