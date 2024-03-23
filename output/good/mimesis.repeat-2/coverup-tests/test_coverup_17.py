# file mimesis/providers/generic.py:106-125
# lines [106, 114, 115, 116, 118, 119, 120, 121, 122, 123, 125]
# branches ['114->115', '114->125', '115->116', '115->118']

import pytest
from mimesis.providers import BaseDataProvider
from mimesis.providers.generic import Generic
import inspect

# Custom provider class for testing
class CustomProvider(BaseDataProvider):
    class Meta:
        name = 'customprovider'

# Custom provider class without Meta
class CustomProviderNoMeta(BaseDataProvider):
    pass

# Non-provider class
class NonProvider:
    pass

# Test function to cover the missing lines/branches
def test_add_provider(mocker):
    generic = Generic()

    # Test adding a valid provider with Meta class
    generic.add_provider(CustomProvider)
    assert hasattr(generic, 'customprovider'), "CustomProvider should be added to Generic"

    # Test adding a valid provider without Meta class
    generic.add_provider(CustomProviderNoMeta)
    assert hasattr(generic, 'customprovidernometa'), "CustomProviderNoMeta should be added to Generic"

    # Test adding a non-class object
    with pytest.raises(TypeError, match='The provider must be a class'):
        generic.add_provider(NonProvider())

    # Test adding a class that is not a subclass of BaseDataProvider
    with pytest.raises(TypeError, match='The provider must be a subclass of BaseProvider'):
        generic.add_provider(NonProvider)

    # Clean up by removing the added providers
    if hasattr(generic, 'customprovider'):
        delattr(generic, 'customprovider')
    if hasattr(generic, 'customprovidernometa'):
        delattr(generic, 'customprovidernometa')
