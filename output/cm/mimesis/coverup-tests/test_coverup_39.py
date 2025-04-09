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
    # Fixture to clean up providers after the test
    yield
    CustomProvider.Meta.name = "custom_provider"

def test_abstract_field_with_providers(cleanup_providers):
    # Test to ensure that providers are added correctly
    field = AbstractField(providers=[CustomProvider])
    assert hasattr(field._gen, 'custom_provider'), "Custom provider should be added to the generator"
    # Check that the custom method returns the expected value
    assert field._gen.custom_provider.custom_method() == "custom_value", "Custom method should return 'custom_value'"
    # Clean up by resetting the provider's name
    CustomProvider.Meta.name = "custom_provider"
