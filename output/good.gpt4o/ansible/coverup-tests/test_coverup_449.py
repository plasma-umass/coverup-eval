# file lib/ansible/playbook/handler_task_include.py:27-39
# lines [27, 29, 31, 32, 33, 34, 35, 36, 39]
# branches []

import pytest
from ansible.playbook.handler_task_include import HandlerTaskInclude
from unittest.mock import Mock

def test_handler_task_include_load(mocker):
    data = {'some_key': 'some_value'}
    block = Mock()
    role = Mock()
    task_include = Mock()
    variable_manager = Mock()
    loader = Mock()

    mocker.patch.object(HandlerTaskInclude, 'check_options', return_value='handler')
    mocker.patch.object(HandlerTaskInclude, 'load_data', return_value='loaded_data')

    handler = HandlerTaskInclude.load(data, block=block, role=role, task_include=task_include, variable_manager=variable_manager, loader=loader)

    HandlerTaskInclude.check_options.assert_called_once_with('loaded_data', data)
    HandlerTaskInclude.load_data.assert_called_once_with(data, variable_manager=variable_manager, loader=loader)
    assert handler == 'handler'
