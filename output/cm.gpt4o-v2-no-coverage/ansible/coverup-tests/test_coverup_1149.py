# file: lib/ansible/playbook/taggable.py:45-89
# asked: {"lines": [55, 74, 82, 83, 87], "branches": [[54, 55], [73, 74], [81, 82], [82, 83], [82, 89], [86, 87]]}
# gained: {"lines": [74], "branches": [[73, 74]]}

import pytest
from unittest.mock import Mock, patch
from ansible.playbook.taggable import Taggable
from ansible.template import Templar

@pytest.fixture
def taggable():
    taggable = Taggable()
    taggable.tags = []
    taggable._loader = Mock()
    taggable._loader.get_basedir = Mock(return_value='.')
    return taggable

def test_evaluate_tags_no_tags(taggable):
    result = taggable.evaluate_tags(only_tags=None, skip_tags=None, all_vars={})
    assert result is True

def test_evaluate_tags_with_tags(taggable, mocker):
    taggable.tags = ['test']
    mock_templar = mocker.patch('ansible.template.Templar.template', return_value=['test'])
    result = taggable.evaluate_tags(only_tags=None, skip_tags=None, all_vars={})
    assert result is True
    mock_templar.assert_called_once_with(['test'])

def test_evaluate_tags_only_tags(taggable, mocker):
    taggable.tags = ['test']
    mocker.patch('ansible.template.Templar.template', return_value=['test'])
    result = taggable.evaluate_tags(only_tags=['test'], skip_tags=None, all_vars={})
    assert result is True

def test_evaluate_tags_skip_tags(taggable, mocker):
    taggable.tags = ['test']
    mocker.patch('ansible.template.Templar.template', return_value=['test'])
    result = taggable.evaluate_tags(only_tags=None, skip_tags=['test'], all_vars={})
    assert result is False

def test_evaluate_tags_only_and_skip_tags(taggable, mocker):
    taggable.tags = ['test']
    mocker.patch('ansible.template.Templar.template', return_value=['test'])
    result = taggable.evaluate_tags(only_tags=['test'], skip_tags=['test'], all_vars={})
    assert result is False

def test_evaluate_tags_always_tag(taggable, mocker):
    taggable.tags = ['always']
    mocker.patch('ansible.template.Templar.template', return_value=['always'])
    result = taggable.evaluate_tags(only_tags=['test'], skip_tags=None, all_vars={})
    assert result is True

def test_evaluate_tags_never_tag(taggable, mocker):
    taggable.tags = ['never']
    mocker.patch('ansible.template.Templar.template', return_value=['never'])
    result = taggable.evaluate_tags(only_tags=['test'], skip_tags=None, all_vars={})
    assert result is False

def test_evaluate_tags_all_tag(taggable, mocker):
    taggable.tags = ['test']
    mocker.patch('ansible.template.Templar.template', return_value=['test'])
    result = taggable.evaluate_tags(only_tags=['all'], skip_tags=None, all_vars={})
    assert result is True

def test_evaluate_tags_tagged_tag(taggable, mocker):
    taggable.tags = ['test']
    mocker.patch('ansible.template.Templar.template', return_value=['test'])
    result = taggable.evaluate_tags(only_tags=['tagged'], skip_tags=None, all_vars={})
    assert result is True

def test_evaluate_tags_untagged(taggable):
    taggable.tags = []
    result = taggable.evaluate_tags(only_tags=['tagged'], skip_tags=None, all_vars={})
    assert result is False
