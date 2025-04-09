# file mimesis/providers/generic.py:34-36
# lines [34, 35]
# branches []

import pytest
from mimesis.providers.generic import Generic
from mimesis.providers.base import BaseDataProvider

def test_generic_inherits_base_data_provider():
    generic_instance = Generic()
    assert isinstance(generic_instance, BaseDataProvider)

@pytest.fixture
def mock_generic(mocker):
    mocker.patch('mimesis.providers.generic.Generic.__init__', return_value=None)
    return Generic()

def test_generic_initialization(mock_generic):
    assert isinstance(mock_generic, Generic)
