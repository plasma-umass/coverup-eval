# file mimesis/providers/generic.py:106-125
# lines [106, 114, 115, 116, 118, 119, 120, 121, 122, 123, 125]
# branches ['114->115', '114->125', '115->116', '115->118']

import pytest
from mimesis.providers.generic import Generic
from mimesis.providers.base import BaseProvider, BaseDataProvider
import inspect

class CustomProvider(BaseProvider):
    class Meta:
        name = 'custom'

class InvalidProvider:
    pass

def test_add_provider_with_valid_provider():
    generic = Generic()
    generic.add_provider(CustomProvider)
    assert hasattr(generic, 'custom')
    assert isinstance(generic.custom, CustomProvider)

def test_add_provider_with_invalid_provider():
    generic = Generic()
    with pytest.raises(TypeError, match='The provider must be a subclass of BaseProvider'):
        generic.add_provider(InvalidProvider)

def test_add_provider_with_non_class():
    generic = Generic()
    with pytest.raises(TypeError, match='The provider must be a class'):
        generic.add_provider('not_a_class')

def test_add_provider_without_meta_name():
    class AnotherProvider(BaseProvider):
        pass

    generic = Generic()
    generic.add_provider(AnotherProvider)
    assert hasattr(generic, 'anotherprovider')
    assert isinstance(generic.anotherprovider, AnotherProvider)
