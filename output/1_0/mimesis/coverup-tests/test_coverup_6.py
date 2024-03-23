# file mimesis/enums.py:26-35
# lines [26, 27, 32, 33, 34, 35]
# branches []

import pytest
from mimesis.enums import PortRange

def test_port_range_enum():
    assert PortRange.ALL.value == (1, 65535)
    assert PortRange.WELL_KNOWN.value == (1, 1023)
    assert PortRange.EPHEMERAL.value == (49152, 65535)
    assert PortRange.REGISTERED.value == (1024, 49151)
