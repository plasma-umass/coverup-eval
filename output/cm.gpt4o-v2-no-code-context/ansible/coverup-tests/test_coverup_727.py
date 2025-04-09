# file: lib/ansible/inventory/host.py:45-46
# asked: {"lines": [45, 46], "branches": []}
# gained: {"lines": [45, 46], "branches": []}

import pytest
from ansible.inventory.host import Host

class TestHost:
    def test_host_ne(self):
        host1 = Host()
        host2 = Host()
        
        # Mock the __eq__ method to control its behavior
        with pytest.MonkeyPatch.context() as mp:
            mp.setattr(host1, "__eq__", lambda other: False)
            assert host1 != host2  # This should trigger the __ne__ method and return True

            mp.setattr(host1, "__eq__", lambda other: True)
            assert not (host1 != host2)  # This should trigger the __ne__ method and return False
