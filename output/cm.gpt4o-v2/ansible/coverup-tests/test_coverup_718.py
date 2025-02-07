# file: lib/ansible/parsing/yaml/constructor.py:91-99
# asked: {"lines": [91, 94, 95, 97, 99], "branches": []}
# gained: {"lines": [91, 94, 95, 97, 99], "branches": []}

import pytest
from unittest.mock import Mock
from ansible.parsing.yaml.constructor import AnsibleConstructor
from ansible.parsing.yaml.objects import AnsibleUnicode
from yaml.nodes import ScalarNode
from yaml.reader import ReaderError
from yaml.error import Mark

@pytest.fixture
def mock_node():
    mark = Mark(name='mock_file', index=0, line=0, column=0, buffer=None, pointer=None)
    return ScalarNode(tag='tag:yaml.org,2002:str', value='test_value', start_mark=mark, end_mark=mark)

def test_construct_yaml_str(mock_node, mocker):
    constructor = AnsibleConstructor()
    mocker.patch.object(constructor, 'construct_scalar', return_value='test_value')
    mocker.patch.object(constructor, '_node_position_info', return_value=('mock_file', 1, 1))

    result = constructor.construct_yaml_str(mock_node)

    assert isinstance(result, AnsibleUnicode)
    assert result == 'test_value'
    assert result.ansible_pos == ('mock_file', 1, 1)
