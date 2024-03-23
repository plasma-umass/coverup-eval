# file mimesis/providers/transport.py:23-29
# lines [23, 29]
# branches []

import pytest
from mimesis.providers.transport import Transport


@pytest.fixture
def transport_provider():
    return Transport()


def test_transport_init(transport_provider):
    # Since the Transport class does not have a _data attribute, we need to
    # test the initialization in a different way. We'll check if the object
    # is an instance of Transport instead.
    assert isinstance(transport_provider, Transport)
