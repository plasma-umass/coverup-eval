# file mimesis/providers/generic.py:106-125
# lines [106, 114, 115, 116, 118, 119, 120, 121, 122, 123, 125]
# branches ['114->115', '114->125', '115->116', '115->118']

import pytest
from mimesis.providers import BaseDataProvider
from mimesis.providers.generic import Generic
import inspect

# Custom provider that does not have a Meta class
class CustomProviderWithoutMeta(BaseDataProvider):
    pass

# Custom provider that has a Meta class with a name attribute
class CustomProviderWithMeta(BaseDataProvider):
    class Meta:
        name = 'custom_with_meta'

# Custom provider that is not a subclass of BaseDataProvider
class NotAProvider:
    pass

def test_add_provider_without_meta(mocker):
    generic = Generic()
    mocker.spy(inspect, 'isclass')
    generic.add_provider(CustomProviderWithoutMeta)
    assert hasattr(generic, 'customproviderwithoutmeta')
    inspect.isclass.assert_called_once_with(CustomProviderWithoutMeta)

def test_add_provider_with_meta(mocker):
    generic = Generic()
    mocker.spy(inspect, 'isclass')
    generic.add_provider(CustomProviderWithMeta)
    assert hasattr(generic, 'custom_with_meta')
    inspect.isclass.assert_called_once_with(CustomProviderWithMeta)

def test_add_provider_raises_type_error_if_not_class():
    generic = Generic()
    with pytest.raises(TypeError, match='The provider must be a class'):
        generic.add_provider(NotAProvider())

def test_add_provider_raises_type_error_if_not_subclass_of_base_provider():
    generic = Generic()
    with pytest.raises(TypeError, match='The provider must be a subclass of BaseProvider'):
        generic.add_provider(NotAProvider)
