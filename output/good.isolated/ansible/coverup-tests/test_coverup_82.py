# file lib/ansible/vars/reserved.py:31-65
# lines [31, 34, 35, 36, 39, 41, 42, 45, 46, 47, 49, 52, 53, 57, 58, 60, 61, 63, 65]
# branches ['41->42', '41->52', '45->41', '45->46', '46->47', '46->49', '52->53', '52->57', '57->58', '57->60', '60->61', '60->63']

import pytest
from ansible.playbook.play import Play
from ansible.playbook.role import Role
from ansible.playbook.block import Block
from ansible.playbook.task import Task

# Assuming the above code is in a file named reserved.py
from ansible.vars.reserved import get_reserved_names

@pytest.fixture
def mock_classes(mocker):
    # Mock the classes to have _attributes with both public and private attributes
    PlayMock = mocker.MagicMock()
    PlayMock.return_value.__dict__['_attributes'] = {'name': None, '_private_field': None}
    RoleMock = mocker.MagicMock()
    RoleMock.return_value.__dict__['_attributes'] = {'tasks': None, '_private_role': None}
    BlockMock = mocker.MagicMock()
    BlockMock.return_value.__dict__['_attributes'] = {'block': None, '_private_block': None}
    TaskMock = mocker.MagicMock()
    TaskMock.return_value.__dict__['_attributes'] = {'action': None, '_private_task': None, 'loop': None}

    mocker.patch('ansible.vars.reserved.Play', new=PlayMock)
    mocker.patch('ansible.vars.reserved.Role', new=RoleMock)
    mocker.patch('ansible.vars.reserved.Block', new=BlockMock)
    mocker.patch('ansible.vars.reserved.Task', new=TaskMock)

    return PlayMock, RoleMock, BlockMock, TaskMock

def test_get_reserved_names_include_private(mock_classes):
    reserved_names = get_reserved_names(include_private=True)
    assert 'name' in reserved_names
    assert '_private_field' in reserved_names
    assert 'tasks' in reserved_names
    assert '_private_role' in reserved_names
    assert 'block' in reserved_names
    assert '_private_block' in reserved_names
    assert 'action' in reserved_names
    assert '_private_task' in reserved_names
    assert 'loop' in reserved_names
    assert 'with_' in reserved_names  # because 'loop' is present
    assert 'local_action' in reserved_names  # because 'action' is present

def test_get_reserved_names_exclude_private(mock_classes):
    reserved_names = get_reserved_names(include_private=False)
    assert 'name' in reserved_names
    assert '_private_field' not in reserved_names
    assert 'tasks' in reserved_names
    assert '_private_role' not in reserved_names
    assert 'block' in reserved_names
    assert '_private_block' not in reserved_names
    assert 'action' in reserved_names
    assert '_private_task' not in reserved_names
    assert 'loop' in reserved_names
    assert 'with_' in reserved_names  # because 'loop' is present
    assert 'local_action' in reserved_names  # because 'action' is present
