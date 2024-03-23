# file mimesis/builtins/de.py:11-33
# lines [11, 12, 14, 16, 17, 19, 20, 22, 24, 30, 31, 33]
# branches []

import pytest
from mimesis.builtins.de import GermanySpecProvider

def test_germany_spec_provider_noun(mocker):
    # Mock the _data attribute to control the output
    mock_data = {
        'noun': ['Haus'],
        'plural': ['Häuser']
    }
    
    # Mock the _pull method to prevent it from modifying _data
    mocker.patch.object(GermanySpecProvider, '_pull', return_value=None)
    
    provider = GermanySpecProvider()
    provider._data = mock_data  # Set the _data attribute directly

    # Test the noun method for singular
    singular_noun = provider.noun()
    assert singular_noun == 'Haus', "The noun should be in singular form."

    # Test the noun method for plural
    plural_noun = provider.noun(plural=True)
    assert plural_noun == 'Häuser', "The noun should be in plural form."
