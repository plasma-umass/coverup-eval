# file lib/ansible/playbook/block.py:149-162
# lines [150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 161, 162]
# branches []

import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.block import Block

# Assuming the existence of the following dependencies in the actual code
# since they are not provided in the snippet above:
# - Base
# - Conditional
# - CollectionSearch
# - Taggable
# - load_list_of_tasks

def test_block_load_always_with_assertion_error(mocker):
    # Mock dependencies
    mocker.patch('ansible.playbook.block.Base')
    mocker.patch('ansible.playbook.block.Conditional')
    mocker.patch('ansible.playbook.block.CollectionSearch')
    mocker.patch('ansible.playbook.block.Taggable')
    mocker.patch('ansible.playbook.block.load_list_of_tasks', side_effect=AssertionError("Test"))

    block = Block()

    # Set necessary instance variables
    block._play = mocker.MagicMock()
    block._role = mocker.MagicMock()
    block._variable_manager = mocker.MagicMock()
    block._loader = mocker.MagicMock()
    block._use_handlers = mocker.MagicMock()
    block._ds = {'always': 'dummy_data'}

    # Test that AnsibleParserError is raised with the correct message
    with pytest.raises(AnsibleParserError) as excinfo:
        block._load_always('always', block._ds)

    assert "A malformed block was encountered while loading always" in str(excinfo.value)
    assert excinfo.value.orig_exc is not None
