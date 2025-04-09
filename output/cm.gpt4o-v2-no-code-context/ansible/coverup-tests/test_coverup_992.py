# file: lib/ansible/playbook/taggable.py:45-89
# asked: {"lines": [55, 68, 73, 74, 76], "branches": [[54, 55], [67, 68], [71, 73], [73, 74], [73, 76], [82, 89], [86, 89]]}
# gained: {"lines": [55, 68, 73, 74], "branches": [[54, 55], [67, 68], [71, 73], [73, 74]]}

import pytest
from unittest.mock import MagicMock
from ansible.playbook.taggable import Taggable

@pytest.fixture
def taggable():
    taggable = Taggable()
    taggable._loader = MagicMock()
    taggable.tags = None
    taggable.untagged = set()
    return taggable

def test_evaluate_tags_with_list_tag(taggable, mocker):
    mocker.patch.object(taggable, 'tags', [['tag1', 'tag2']])
    templar_mock = mocker.patch('ansible.playbook.taggable.Templar')
    templar_instance = templar_mock.return_value
    templar_instance.template.return_value = [['tag1', 'tag2']]
    
    result = taggable.evaluate_tags(only_tags=None, skip_tags=None, all_vars={})
    
    assert result is True
    assert set(taggable.tags) == {'tag1', 'tag2'}

def test_evaluate_tags_with_always_in_tags(taggable, mocker):
    mocker.patch.object(taggable, 'tags', ['always'])
    templar_mock = mocker.patch('ansible.playbook.taggable.Templar')
    templar_instance = templar_mock.return_value
    templar_instance.template.return_value = ['always']
    
    result = taggable.evaluate_tags(only_tags=['some_tag'], skip_tags=None, all_vars={})
    
    assert result is True

def test_evaluate_tags_with_tagged_in_only_tags(taggable, mocker):
    mocker.patch.object(taggable, 'tags', ['some_tag'])
    templar_mock = mocker.patch('ansible.playbook.taggable.Templar')
    templar_instance = templar_mock.return_value
    templar_instance.template.return_value = ['some_tag']
    
    result = taggable.evaluate_tags(only_tags=['tagged'], skip_tags=None, all_vars={})
    
    assert result is True

def test_evaluate_tags_with_all_in_skip_tags(taggable, mocker):
    mocker.patch.object(taggable, 'tags', ['always'])
    templar_mock = mocker.patch('ansible.playbook.taggable.Templar')
    templar_instance = templar_mock.return_value
    templar_instance.template.return_value = ['always']
    
    result = taggable.evaluate_tags(only_tags=None, skip_tags=['all', 'always'], all_vars={})
    
    assert result is False

def test_evaluate_tags_with_tagged_in_skip_tags(taggable, mocker):
    mocker.patch.object(taggable, 'tags', ['some_tag'])
    templar_mock = mocker.patch('ansible.playbook.taggable.Templar')
    templar_instance = templar_mock.return_value
    templar_instance.template.return_value = ['some_tag']
    
    result = taggable.evaluate_tags(only_tags=None, skip_tags=['tagged'], all_vars={})
    
    assert result is False
