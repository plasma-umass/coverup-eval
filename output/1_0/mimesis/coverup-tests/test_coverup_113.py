# file mimesis/providers/transport.py:71-83
# lines [81, 82, 83]
# branches []

import pytest
from mimesis.providers.transport import Transport

@pytest.fixture
def transport():
    return Transport()

def test_airplane_model(transport, mocker):
    model_mask = '####'
    mocker.patch.object(transport.random, 'custom_code', return_value='1234')
    mocker.patch.object(transport.random, 'choice', return_value='Boeing')
    model = transport.airplane(model_mask=model_mask)
    assert model.startswith('Boeing')
    assert model.endswith('1234')
