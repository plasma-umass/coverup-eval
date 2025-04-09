# file mimesis/providers/text.py:146-159
# lines [146, 155, 156, 158, 159]
# branches ['155->156', '155->158']

import pytest
from mimesis.providers.text import Text

def test_hex_color_safe(mocker):
    text_provider = Text()
    mocker.patch.object(text_provider.random, 'choice', return_value='#ff5733')
    
    result = text_provider.hex_color(safe=True)
    
    assert result == '#ff5733'

def test_hex_color_non_safe(mocker):
    text_provider = Text()
    mocker.patch.object(text_provider.random, 'randint', return_value=0xd8346b)
    
    result = text_provider.hex_color(safe=False)
    
    assert result == '#d8346b'
