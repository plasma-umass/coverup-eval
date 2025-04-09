# file: lib/ansible/inventory/host.py:51-52
# asked: {"lines": [51, 52], "branches": []}
# gained: {"lines": [51, 52], "branches": []}

import pytest
from ansible.inventory.host import Host

class TestHost:
    def test_str_method(self, mocker):
        # Arrange
        host = Host()
        mock_get_name = mocker.patch.object(host, 'get_name', return_value='test_host')

        # Act
        result = str(host)

        # Assert
        mock_get_name.assert_called_once()
        assert result == 'test_host'
