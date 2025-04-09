# file lib/ansible/parsing/utils/yaml.py:46-56
# lines [46, 49, 50, 51, 53, 54, 55, 56]
# branches []

import pytest
from ansible.parsing.utils.yaml import AnsibleLoader, _safe_load
from yaml import YAMLError

# Mocking the stream to raise an AttributeError on dispose to test the except block
class MockLoaderWithDisposeError(AnsibleLoader):
    def dispose(self):
        raise AttributeError("Mocked dispose error")

@pytest.fixture
def mock_loader(mocker):
    mocker.patch('ansible.parsing.utils.yaml.AnsibleLoader', MockLoaderWithDisposeError)

def test_safe_load_with_dispose_error(mock_loader):
    fake_stream = "fake_stream_content"
    # No need to assert anything as we are testing the exception handling
    # and just want to ensure the AttributeError is caught and ignored
    _safe_load(fake_stream)  # This should not raise an AttributeError
