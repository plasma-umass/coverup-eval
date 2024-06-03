# file cookiecutter/replay.py:19-36
# lines [19, 21, 22, 24, 25, 27, 28, 30, 31, 33, 35, 36]
# branches ['21->22', '21->24', '24->25', '24->27', '27->28', '27->30', '30->31', '30->33']

import pytest
import json
import os
from unittest import mock
from cookiecutter.replay import dump

def test_dump_creates_replay_file(mocker):
    replay_dir = 'test_replay_dir'
    template_name = 'test_template'
    context = {'cookiecutter': {'project_name': 'test_project'}}
    
    mocker.patch('cookiecutter.replay.make_sure_path_exists', return_value=True)
    mocker.patch('cookiecutter.replay.get_file_name', return_value=os.path.join(replay_dir, template_name + '.json'))
    
    if not os.path.exists(replay_dir):
        os.makedirs(replay_dir)
    
    try:
        dump(replay_dir, template_name, context)
        
        replay_file = os.path.join(replay_dir, template_name + '.json')
        assert os.path.exists(replay_file)
        
        with open(replay_file, 'r') as f:
            data = json.load(f)
            assert data == context
    finally:
        if os.path.exists(replay_file):
            os.remove(replay_file)
        if os.path.exists(replay_dir):
            os.rmdir(replay_dir)

def test_dump_raises_ioerror(mocker):
    replay_dir = 'test_replay_dir'
    template_name = 'test_template'
    context = {'cookiecutter': {'project_name': 'test_project'}}
    
    mocker.patch('cookiecutter.replay.make_sure_path_exists', return_value=False)
    
    with pytest.raises(IOError):
        dump(replay_dir, template_name, context)

def test_dump_raises_typeerror_for_template_name():
    replay_dir = 'test_replay_dir'
    template_name = 123  # Not a string
    context = {'cookiecutter': {'project_name': 'test_project'}}
    
    with pytest.raises(TypeError):
        dump(replay_dir, template_name, context)

def test_dump_raises_typeerror_for_context():
    replay_dir = 'test_replay_dir'
    template_name = 'test_template'
    context = ['not', 'a', 'dict']  # Not a dictionary
    
    with pytest.raises(TypeError):
        dump(replay_dir, template_name, context)

def test_dump_raises_valueerror_for_missing_cookiecutter_key():
    replay_dir = 'test_replay_dir'
    template_name = 'test_template'
    context = {'not_cookiecutter': {'project_name': 'test_project'}}
    
    with pytest.raises(ValueError):
        dump(replay_dir, template_name, context)
