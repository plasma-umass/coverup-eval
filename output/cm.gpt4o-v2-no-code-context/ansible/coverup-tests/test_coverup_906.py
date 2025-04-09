# file: lib/ansible/parsing/yaml/dumper.py:53-54
# asked: {"lines": [53, 54], "branches": []}
# gained: {"lines": [53], "branches": []}

import pytest
import yaml
from ansible.parsing.yaml.dumper import AnsibleDumper

class TestAnsibleDumper:
    def test_represent_binary(self, monkeypatch):
        # Create a mock for the binary_type function
        def mock_binary_type(data):
            return data

        # Patch the binary_type function in the module where AnsibleDumper is defined
        monkeypatch.setattr('ansible.parsing.yaml.dumper.binary_type', mock_binary_type)

        # Create a mock stream to pass to AnsibleDumper
        class MockStream:
            def write(self, data):
                pass

        # Create an instance of AnsibleDumper with a mock stream
        mock_stream = MockStream()
        dumper = AnsibleDumper(mock_stream)

        # Create a binary data to test
        binary_data = b'test binary data'

        # Call the represent_binary method
        result = dumper.represent_binary(binary_data)

        # Assert that the result is as expected
        expected_result = yaml.representer.SafeRepresenter.represent_binary(dumper, binary_data)
        assert result.tag == expected_result.tag
        assert result.value == expected_result.value
