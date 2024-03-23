# file lib/ansible/parsing/yaml/loader.py:29-33
# lines [29, 30, 31, 32, 33]
# branches []

import pytest
from ansible.parsing.yaml.loader import AnsibleLoader
from io import StringIO

@pytest.fixture
def mock_stream():
    return StringIO('dummy_content')

@pytest.fixture
def mock_ansible_constructor(mocker):
    return mocker.patch('ansible.parsing.yaml.loader.AnsibleConstructor.__init__', return_value=None)

@pytest.fixture
def mock_resolver(mocker):
    return mocker.patch('ansible.parsing.yaml.loader.Resolver.__init__', return_value=None)

def test_ansible_loader_init(mock_stream, mock_ansible_constructor, mock_resolver):
    # Given a mock stream and file name
    stream = mock_stream
    file_name = 'test_file.yml'
    vault_secrets = 'vault_secret'

    # When initializing AnsibleLoader
    loader = AnsibleLoader(stream, file_name=file_name, vault_secrets=vault_secrets)

    # Then the AnsibleConstructor, and Resolver should be initialized properly
    mock_ansible_constructor.assert_called_once_with(loader, file_name=file_name, vault_secrets=vault_secrets)
    mock_resolver.assert_called_once_with(loader)

    # Cleanup is handled by pytest fixtures
