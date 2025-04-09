# file lib/ansible/vars/reserved.py:31-65
# lines [31, 34, 35, 36, 39, 41, 42, 45, 46, 47, 49, 52, 53, 57, 58, 60, 61, 63, 65]
# branches ['41->42', '41->52', '45->41', '45->46', '46->47', '46->49', '52->53', '52->57', '57->58', '57->60', '60->61', '60->63']

import pytest
from unittest.mock import patch

# Mock classes to simulate Play, Role, Block, Task
class MockClass:
    def __init__(self, attributes):
        self.__dict__['_attributes'] = attributes

@pytest.fixture
def mock_classes(mocker):
    mocker.patch('ansible.vars.reserved.Play', return_value=MockClass(['action', 'private_attr', 'loop']))
    mocker.patch('ansible.vars.reserved.Role', return_value=MockClass(['role_attr', 'private_role_attr']))
    mocker.patch('ansible.vars.reserved.Block', return_value=MockClass(['block_attr', 'private_block_attr']))
    mocker.patch('ansible.vars.reserved.Task', return_value=MockClass(['task_attr', 'private_task_attr']))

def test_get_reserved_names_include_private(mock_classes):
    from ansible.vars.reserved import get_reserved_names

    result = get_reserved_names(include_private=True)
    expected_public = {'action', 'local_action', 'role_attr', 'block_attr', 'task_attr', 'with_', 'loop'}
    expected_private = {'private_attr', 'private_role_attr', 'private_block_attr', 'private_task_attr'}
    expected_result = expected_public.union(expected_private)

    assert result == expected_result

def test_get_reserved_names_exclude_private(mock_classes):
    from ansible.vars.reserved import get_reserved_names

    result = get_reserved_names(include_private=False)
    expected_result = {'action', 'local_action', 'role_attr', 'block_attr', 'task_attr', 'with_', 'loop'}

    assert result == expected_result
