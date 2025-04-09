# file: lib/ansible/parsing/utils/yaml.py:46-56
# asked: {"lines": [46, 49, 50, 51, 53, 54, 55, 56], "branches": []}
# gained: {"lines": [46, 49, 50, 51, 53, 54, 55, 56], "branches": []}

import pytest
from ansible.parsing.yaml.loader import AnsibleLoader
from ansible.parsing.utils.yaml import _safe_load
from unittest.mock import Mock, patch

@pytest.fixture
def mock_loader(mocker):
    mocker.patch('ansible.parsing.yaml.loader.AnsibleLoader.get_single_data', return_value='mocked_data')
    mocker.patch('ansible.parsing.yaml.loader.AnsibleLoader.dispose')

def test_safe_load_success(mock_loader):
    stream = "mock_stream"
    result = _safe_load(stream)
    assert result == 'mocked_data'
    AnsibleLoader.get_single_data.assert_called_once()
    AnsibleLoader.dispose.assert_called_once()

def test_safe_load_dispose_attribute_error(mocker):
    stream = "mock_stream"
    mocker.patch('ansible.parsing.yaml.loader.AnsibleLoader.dispose', side_effect=AttributeError)
    mocker.patch('ansible.parsing.yaml.loader.AnsibleLoader.get_single_data', return_value='mocked_data')
    result = _safe_load(stream)
    assert result == 'mocked_data'
    AnsibleLoader.get_single_data.assert_called_once()
    AnsibleLoader.dispose.assert_called_once()
