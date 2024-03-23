# file mimesis/providers/structure.py:22-30
# lines [22, 28, 29, 30]
# branches []

import pytest
from mimesis.providers import Structure
from mimesis.providers.internet import Internet
from mimesis.providers.text import Text

def test_structure_initialization(mocker):
    # Mock the Internet and Text classes to ensure they are called with correct parameters
    internet_mock = mocker.patch('mimesis.providers.structure.Internet', autospec=True)
    text_mock = mocker.patch('mimesis.providers.structure.Text', autospec=True)

    seed = 12345
    locale = 'en'
    structure = Structure(locale=locale, seed=seed)

    # Check if Internet and Text were initialized with the correct seed
    internet_mock.assert_called_once_with(seed=seed)
    text_mock.assert_called_once_with(locale, seed=seed)
