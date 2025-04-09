# file: lib/ansible/inventory/host.py:54-55
# asked: {"lines": [54, 55], "branches": []}
# gained: {"lines": [54, 55], "branches": []}

import pytest
from ansible.inventory.host import Host

class TestHost:
    def test_repr(self, mocker):
        # Arrange
        host = Host()
        mock_get_name = mocker.patch.object(host, 'get_name', return_value='test_host')

        # Act
        result = repr(host)

        # Assert
        mock_get_name.assert_called_once()
        assert result == 'test_host'
