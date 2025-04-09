# file mimesis/providers/structure.py:22-30
# lines [22, 28, 29, 30]
# branches []

import pytest
from mimesis.providers.structure import Structure
from mimesis.providers.internet import Internet
from mimesis.providers.text import Text

def test_structure_initialization(mocker):
    mock_internet = mocker.patch('mimesis.providers.structure.Internet', autospec=True)
    mock_text = mocker.patch('mimesis.providers.structure.Text', autospec=True)

    structure = Structure(locale='en', seed=42)

    mock_internet.assert_called_once_with(seed=42)
    mock_text.assert_called_once_with('en', seed=42)

    assert isinstance(structure, Structure)
    assert structure._Structure__inet is mock_internet.return_value
    assert structure._Structure__text is mock_text.return_value
