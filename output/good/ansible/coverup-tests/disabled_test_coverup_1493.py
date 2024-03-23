# file lib/ansible/playbook/play.py:104-119
# lines []
# branches ['106->exit']

import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.play import Play
from ansible.module_utils.six import text_type, binary_type

# Assuming the existence of a mock for the Base class and CollectionSearch
# If these do not exist, they would need to be created for the test to work

class TestPlay:
    @pytest.fixture
    def mock_play(self, mocker):
        # Mocking the Base and CollectionSearch classes directly within the Play class
        mocker.patch('ansible.playbook.play.Base', create=True)
        mocker.patch('ansible.playbook.play.CollectionSearch', create=True)
        play = Play()
        play._ds = {'hosts': True}  # Simulate that 'hosts' key exists in _ds
        return play

    def test_validate_hosts_with_invalid_type(self, mock_play):
        with pytest.raises(AnsibleParserError) as excinfo:
            mock_play._validate_hosts('hosts', 'hosts', 123)  # Pass an invalid type (not sequence or string)
        assert "Hosts list must be a sequence or string." in str(excinfo.value)

        with pytest.raises(AnsibleParserError) as excinfo:
            mock_play._validate_hosts('hosts', 'hosts', [123])  # Pass a sequence with an invalid type
        assert "Hosts list contains an invalid host value:" in str(excinfo.value)

        with pytest.raises(AnsibleParserError) as excinfo:
            mock_play._validate_hosts('hosts', 'hosts', [None])  # Pass a sequence with None
        assert "Hosts list cannot contain values of 'None'." in str(excinfo.value)

        with pytest.raises(AnsibleParserError) as excinfo:
            mock_play._validate_hosts('hosts', 'hosts', None)  # Pass None directly
        assert "Hosts list cannot be empty." in str(excinfo.value)

        # Test to cover branch 106->exit when 'hosts' is not in self._ds
        play_without_hosts = Play()
        play_without_hosts._ds = {}  # 'hosts' key does not exist in _ds
        # No exception should be raised in this case, so no need for a context manager
        play_without_hosts._validate_hosts('hosts', 'hosts', 'all')  # Pass a valid string

        # Cleanup is handled by pytest fixtures automatically
