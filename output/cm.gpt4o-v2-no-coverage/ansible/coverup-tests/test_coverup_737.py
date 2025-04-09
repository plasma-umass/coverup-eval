# file: lib/ansible/parsing/yaml/constructor.py:91-99
# asked: {"lines": [91, 94, 95, 97, 99], "branches": []}
# gained: {"lines": [91, 94, 95, 97, 99], "branches": []}

import pytest
from unittest.mock import Mock
from ansible.parsing.yaml.constructor import AnsibleConstructor
from ansible.parsing.yaml.objects import AnsibleUnicode
from yaml.nodes import ScalarNode

@pytest.fixture
def mock_node():
    return Mock(spec=ScalarNode)

@pytest.fixture
def constructor():
    return AnsibleConstructor()

def test_construct_yaml_str(monkeypatch, constructor, mock_node):
    # Mock the methods used within construct_yaml_str
    monkeypatch.setattr(constructor, 'construct_scalar', lambda node: 'test_value')
    monkeypatch.setattr(constructor, '_node_position_info', lambda node: ('test_source', 1, 1))

    result = constructor.construct_yaml_str(mock_node)

    assert isinstance(result, AnsibleUnicode)
    assert result == 'test_value'
    assert result.ansible_pos == ('test_source', 1, 1)
