# file lib/ansible/module_utils/common/network.py:19-29
# lines [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
# branches ['21->22', '21->23', '23->24', '23->29', '25->23', '25->26']

import pytest
from ansible.module_utils.common.network import is_netmask

VALID_MASKS = [0, 128, 192, 224, 240, 248, 252, 254, 255]

@pytest.mark.parametrize("netmask, expected", [
    ("255.255.255.0", True),
    ("255.255.0.0", True),
    ("255.0.0.0", True),
    ("255.255.255.255", True),
    ("255.255.255.256", False),
    ("255.255.255.-1", False),
    ("255.255", False),
    ("255.255.255.255.255", False),
    ("not.a.netmask", False),
    ("", False),
    (None, False),
    (24, False),
    ("255.255.255.254", True),
    ("256.255.255.255", False),
    ("255.256.255.255", False),
    ("255.255.256.255", False),
    ("255.255.255.256", False),
])
def test_is_netmask(netmask, expected):
    assert is_netmask(netmask) == expected
