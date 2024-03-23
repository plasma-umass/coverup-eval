# file cookiecutter/replay.py:19-36
# lines [19, 21, 22, 24, 25, 27, 28, 30, 31, 33, 35, 36]
# branches ['21->22', '21->24', '24->25', '24->27', '27->28', '27->30', '30->31', '30->33']

import json
import os
import pytest
from cookiecutter.replay import dump, get_file_name
from cookiecutter.utils import make_sure_path_exists

@pytest.fixture
def mock_make_sure_path_exists(mocker):
    return mocker.patch('cookiecutter.replay.make_sure_path_exists', return_value=True)

@pytest.fixture
def replay_dir(tmp_path):
    dir_path = tmp_path / "replay"
    dir_path.mkdir()
    return str(dir_path)

@pytest.fixture
def template_name():
    return "test_template"

@pytest.fixture
def context():
    return {"cookiecutter": {"project_slug": "test_project"}}

def test_dump_creates_replay_file(mock_make_sure_path_exists, replay_dir, template_name, context):
    dump(replay_dir, template_name, context)
    replay_file = get_file_name(replay_dir, template_name)
    assert os.path.exists(replay_file)
    with open(replay_file, 'r') as f:
        data = json.load(f)
    assert data == context

def test_dump_raises_ioerror_if_replay_dir_creation_fails(mocker, replay_dir, template_name, context):
    mocker.patch('cookiecutter.replay.make_sure_path_exists', return_value=False)
    with pytest.raises(IOError):
        dump(replay_dir, template_name, context)

def test_dump_raises_typeerror_if_template_name_not_str(replay_dir, context):
    with pytest.raises(TypeError):
        dump(replay_dir, 123, context)

def test_dump_raises_typeerror_if_context_not_dict(replay_dir, template_name):
    with pytest.raises(TypeError):
        dump(replay_dir, template_name, "not_a_dict")

def test_dump_raises_valueerror_if_context_missing_cookiecutter_key(replay_dir, template_name):
    with pytest.raises(ValueError):
        dump(replay_dir, template_name, {})
