# file mimesis/providers/internet.py:289-302
# lines [289, 299, 300, 302]
# branches ['299->300', '299->302']

import pytest
from mimesis.providers.internet import Internet, PortRange
from mimesis.exceptions import NonEnumerableError

def test_port_valid_range():
    internet = Internet()
    port = internet.port(PortRange.WELL_KNOWN)
    assert 0 <= port <= 1023

def test_port_invalid_range():
    internet = Internet()
    with pytest.raises(NonEnumerableError):
        internet.port("invalid_range")
