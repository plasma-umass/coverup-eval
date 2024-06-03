# file mimesis/schema.py:30-45
# lines [30, 31, 32, 38, 39, 40, 42, 43, 45]
# branches ['42->43', '42->45']

import pytest
from mimesis.schema import AbstractField
from mimesis import Generic

def test_abstract_field_initialization(mocker):
    # Mock the Generic class to ensure it is called with the correct parameters
    mock_generic = mocker.patch('mimesis.schema.Generic', autospec=True)
    
    # Test initialization without providers
    locale = 'en'
    seed = 42
    field = AbstractField(locale=locale, seed=seed)
    
    # Assertions to verify the initialization
    assert field.locale == locale
    assert field.seed == seed
    mock_generic.assert_called_once_with(locale, seed)
    assert field._table == {}
    
    # Test initialization with providers
    mock_generic.reset_mock()
    providers = ['provider1', 'provider2']
    field_with_providers = AbstractField(locale=locale, seed=seed, providers=providers)
    
    # Assertions to verify the initialization with providers
    assert field_with_providers.locale == locale
    assert field_with_providers.seed == seed
    mock_generic.assert_called_once_with(locale, seed)
    mock_generic.return_value.add_providers.assert_called_once_with(*providers)
    assert field_with_providers._table == {}
