# file mimesis/providers/internet.py:289-302
# lines [289, 299, 300, 302]
# branches ['299->300', '299->302']

import pytest
from mimesis.exceptions import NonEnumerableError
from mimesis.providers.internet import Internet
from mimesis.enums import PortRange

def test_internet_port_with_valid_range():
    internet = Internet()
    port = internet.port(PortRange.ALL)
    assert port >= PortRange.ALL.value[0] and port <= PortRange.ALL.value[1]

def test_internet_port_with_invalid_range():
    internet = Internet()
    with pytest.raises(NonEnumerableError):
        internet.port("invalid_range")

def test_internet_port_with_specific_range():
    internet = Internet()
    port = internet.port(PortRange.WELL_KNOWN)
    assert port >= PortRange.WELL_KNOWN.value[0] and port <= PortRange.WELL_KNOWN.value[1]

    port = internet.port(PortRange.EPHEMERAL)
    assert port >= PortRange.EPHEMERAL.value[0] and port <= PortRange.EPHEMERAL.value[1]

    port = internet.port(PortRange.REGISTERED)
    assert port >= PortRange.REGISTERED.value[0] and port <= PortRange.REGISTERED.value[1]
