# file mimesis/enums.py:94-106
# lines [94, 95, 100, 101, 102, 103, 104, 105, 106]
# branches []

import pytest
from mimesis.enums import Layer

def test_layer_enum():
    # Assert that all enum members are present and their values are correct
    assert Layer.APPLICATION.value == 'application'
    assert Layer.DATA_LINK.value == 'data_link'
    assert Layer.NETWORK.value == 'network'
    assert Layer.PHYSICAL.value == 'physical'
    assert Layer.PRESENTATION.value == 'presentation'
    assert Layer.SESSION.value == 'session'
    assert Layer.TRANSPORT.value == 'transport'

    # Assert that all enum members are unique
    assert len(Layer) == len(set(Layer))
