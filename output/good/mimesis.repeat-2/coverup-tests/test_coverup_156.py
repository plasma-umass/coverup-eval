# file mimesis/providers/internet.py:289-302
# lines [302]
# branches ['299->302']

import pytest
from mimesis.enums import PortRange
from mimesis.exceptions import NonEnumerableError
from mimesis.providers.internet import Internet

def test_internet_port_with_invalid_port_range(mocker):
    internet = Internet()
    with pytest.raises(NonEnumerableError):
        internet.port(port_range="invalid_port_range")

def test_internet_port_with_valid_port_range(mocker):
    internet = Internet()
    port = internet.port(port_range=PortRange.ALL)
    assert isinstance(port, int)
    assert 0 <= port <= 65535
