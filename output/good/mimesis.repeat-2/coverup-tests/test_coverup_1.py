# file mimesis/schema.py:30-45
# lines [30, 31, 32, 38, 39, 40, 42, 43, 45]
# branches ['42->43', '42->45']

import pytest
from mimesis.schema import AbstractField
from mimesis.providers import BaseProvider

class CustomProvider(BaseProvider):
    class Meta:
        name = "custom_provider"

    def custom_method(self):
        return "custom_value"

@pytest.fixture
def cleanup_providers():
    yield
    CustomProvider.Meta.name = "custom_provider"

def test_abstract_field_with_providers(cleanup_providers, mocker):
    mocker.patch('mimesis.schema.Generic.add_providers')
    custom_provider = CustomProvider()
    field = AbstractField(providers=[custom_provider])
    field._gen.add_providers.assert_called_once_with(custom_provider)
    assert field.locale == 'en'
    assert field.seed is None
    assert field._table == {}
