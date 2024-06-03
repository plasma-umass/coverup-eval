# file lib/ansible/playbook/play.py:133-138
# lines [135, 136, 137, 138]
# branches ['136->137', '136->138']

import pytest
from ansible.playbook.play import Play

def test_play_load_with_vars(mocker):
    data = {'some': 'data'}
    variable_manager = mocker.Mock()
    loader = mocker.Mock()
    vars = {'key': 'value'}

    mock_load_data = mocker.patch.object(Play, 'load_data', return_value='loaded_data')

    play_instance = Play.load(data, variable_manager=variable_manager, loader=loader, vars=vars)

    mock_load_data.assert_called_once_with(data, variable_manager=variable_manager, loader=loader)
    assert mock_load_data.call_args[0][0] == data
    assert mock_load_data.call_args[1]['variable_manager'] == variable_manager
    assert mock_load_data.call_args[1]['loader'] == loader

    # Create a new Play instance to check the vars attribute
    play_instance_check = Play()
    if vars:
        play_instance_check.vars = vars.copy()

    assert play_instance_check.vars == vars
