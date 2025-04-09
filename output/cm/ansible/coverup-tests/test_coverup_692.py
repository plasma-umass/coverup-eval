# file lib/ansible/parsing/yaml/constructor.py:135-147
# lines [135, 138, 139, 145, 147]
# branches []

import pytest
from ansible.parsing.yaml.constructor import AnsibleConstructor
from yaml import Mark

@pytest.fixture
def mock_ansible_constructor(mocker):
    mocker.patch.object(AnsibleConstructor, '__init__', return_value=None)
    ac = AnsibleConstructor()
    ac._ansible_file_name = None
    return ac

def test_node_position_info_with_string_source(mock_ansible_constructor, mocker):
    fake_node = mocker.Mock()
    fake_node.start_mark = Mark('<string>', 0, 42, 43, None, None)
    datasource, line, column = mock_ansible_constructor._node_position_info(fake_node)
    assert datasource == '<string>'
    assert line == 43
    assert column == 44

def test_node_position_info_with_file_source(mock_ansible_constructor, mocker):
    mock_ansible_constructor._ansible_file_name = 'fake_file.yml'
    fake_node = mocker.Mock()
    fake_node.start_mark = Mark('fake_file.yml', 0, 99, 100, None, None)
    datasource, line, column = mock_ansible_constructor._node_position_info(fake_node)
    assert datasource == 'fake_file.yml'
    assert line == 100
    assert column == 101
