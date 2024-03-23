# file mimesis/providers/generic.py:127-134
# lines [133, 134]
# branches ['133->exit', '133->134']

import pytest
from mimesis.providers import BaseProvider
from mimesis.providers.generic import Generic

class CustomProvider(BaseProvider):
    class Meta:
        name = "custom_provider"

@pytest.fixture
def generic_provider():
    return Generic()

def test_add_providers_executes_lines(generic_provider, mocker):
    mocker.spy(generic_provider, 'add_provider')
    custom_providers = [CustomProvider, CustomProvider]
    generic_provider.add_providers(*custom_providers)
    assert generic_provider.add_provider.call_count == len(custom_providers)
    for provider in custom_providers:
        generic_provider.add_provider.assert_any_call(provider)
