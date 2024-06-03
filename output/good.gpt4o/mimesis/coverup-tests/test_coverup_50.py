# file mimesis/providers/generic.py:127-134
# lines [127, 133, 134]
# branches ['133->exit', '133->134']

import pytest
from mimesis.providers.generic import Generic
from mimesis.providers.base import BaseProvider

class CustomProvider(BaseProvider):
    class Meta:
        name = "custom_provider"
    
    def custom_method(self):
        return "custom_value"

def test_add_providers(mocker):
    generic = Generic()
    custom_provider_class = CustomProvider
    
    mock_add_provider = mocker.patch.object(generic, 'add_provider', wraps=generic.add_provider)
    
    generic.add_providers(custom_provider_class)
    
    mock_add_provider.assert_called_once_with(custom_provider_class)
    assert hasattr(generic, 'custom_provider')
    assert generic.custom_provider.custom_method() == "custom_value"
