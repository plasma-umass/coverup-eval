# file mimesis/providers/generic.py:106-125
# lines [106, 114, 115, 116, 118, 119, 120, 121, 122, 123, 125]
# branches ['114->115', '114->125', '115->116', '115->118']

import pytest
from mimesis.providers import BaseDataProvider
from mimesis.providers.generic import Generic

# Custom provider class for testing
class CustomProvider(BaseDataProvider):
    class Meta:
        name = "customprovider"

# Custom provider class without Meta
class CustomProviderNoMeta(BaseDataProvider):
    pass

# Incorrect provider class (not a subclass of BaseDataProvider)
class IncorrectProvider:
    pass

# Test function to cover the missing branches
def test_add_provider():
    generic = Generic()

    # Test adding a correct provider with Meta class
    generic.add_provider(CustomProvider)
    assert hasattr(generic, 'customprovider'), "CustomProvider should be added to Generic"

    # Test adding a correct provider without Meta class
    generic.add_provider(CustomProviderNoMeta)
    assert hasattr(generic, 'customprovidernometa'), "CustomProviderNoMeta should be added to Generic"

    # Test adding a non-class as provider
    with pytest.raises(TypeError) as exc_info:
        generic.add_provider(123)
    assert str(exc_info.value) == 'The provider must be a class'

    # Test adding a class that is not a subclass of BaseDataProvider
    with pytest.raises(TypeError) as exc_info:
        generic.add_provider(IncorrectProvider)
    assert str(exc_info.value) == 'The provider must be a subclass of BaseProvider'

    # Clean up after test
    if hasattr(generic, 'customprovider'):
        delattr(generic, 'customprovider')
    if hasattr(generic, 'customprovidernometa'):
        delattr(generic, 'customprovidernometa')
