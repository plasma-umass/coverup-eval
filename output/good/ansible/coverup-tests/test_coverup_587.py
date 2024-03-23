# file lib/ansible/inventory/host.py:40-43
# lines [40, 41, 42, 43]
# branches ['41->42', '41->43']

import pytest
from ansible.inventory.host import Host

# Assuming the Host class has a uuid attribute or a way to set it, if not this test needs to be adjusted accordingly.

def test_host_eq(mocker):
    # Setup two different Host instances with the same uuid
    uuid = "test-uuid"
    host1 = Host()
    host2 = Host()
    mocker.patch.object(host1, '_uuid', uuid)
    mocker.patch.object(host2, '_uuid', uuid)

    # Test equality of the same object
    assert host1 == host1, "Host object should be equal to itself"

    # Test equality of two different objects with the same uuid
    assert host1 == host2, "Host objects with the same uuid should be equal"

    # Test inequality with a different type
    assert not (host1 == 123), "Host object should not be equal to an object of a different type"

    # Test inequality with a different Host object
    host3 = Host()
    mocker.patch.object(host3, '_uuid', "different-uuid")
    assert not (host1 == host3), "Host objects with different uuids should not be equal"

# Note: No cleanup is necessary as we're using mocker to patch object attributes, which is automatically undone at the end of the test.
