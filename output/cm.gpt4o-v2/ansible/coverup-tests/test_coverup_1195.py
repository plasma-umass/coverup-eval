# file: lib/ansible/playbook/taggable.py:45-89
# asked: {"lines": [55, 74, 82, 83, 87], "branches": [[54, 55], [73, 74], [81, 82], [82, 83], [82, 89], [86, 87]]}
# gained: {"lines": [55, 74, 82, 83, 87], "branches": [[54, 55], [73, 74], [81, 82], [82, 83], [86, 87]]}

import pytest
from ansible.playbook.taggable import Taggable
from ansible.template import Templar

@pytest.fixture
def taggable_instance(mocker):
    instance = Taggable()
    instance._loader = mocker.Mock()
    instance._loader.get_basedir = mocker.Mock(return_value='/tmp')
    instance.tags = []
    return instance

def test_evaluate_tags_with_list_tags(taggable_instance, mocker):
    mocker.patch.object(Templar, 'template', return_value=[['tag1', 'tag2'], 'tag3'])
    only_tags = set()
    skip_tags = set()
    all_vars = {}

    taggable_instance.tags = [['tag1', 'tag2'], 'tag3']
    result = taggable_instance.evaluate_tags(only_tags, skip_tags, all_vars)

    assert result is True
    assert set(taggable_instance.tags) == {'tag1', 'tag2', 'tag3'}

def test_evaluate_tags_with_tagged_only_tags(taggable_instance, mocker):
    mocker.patch.object(Templar, 'template', return_value=['tag1'])
    only_tags = {'tagged'}
    skip_tags = set()
    all_vars = {}

    taggable_instance.tags = ['tag1']
    result = taggable_instance.evaluate_tags(only_tags, skip_tags, all_vars)

    assert result is True

def test_evaluate_tags_with_skip_tags_all(taggable_instance, mocker):
    mocker.patch.object(Templar, 'template', return_value=['tag1'])
    only_tags = set()
    skip_tags = {'all'}
    all_vars = {}

    taggable_instance.tags = ['tag1']
    result = taggable_instance.evaluate_tags(only_tags, skip_tags, all_vars)

    assert result is False

def test_evaluate_tags_with_skip_tags_always(taggable_instance, mocker):
    mocker.patch.object(Templar, 'template', return_value=['always'])
    only_tags = set()
    skip_tags = {'all', 'always'}
    all_vars = {}

    taggable_instance.tags = ['always']
    result = taggable_instance.evaluate_tags(only_tags, skip_tags, all_vars)

    assert result is False

def test_evaluate_tags_with_skip_tags_tagged(taggable_instance, mocker):
    mocker.patch.object(Templar, 'template', return_value=['tag1'])
    only_tags = set()
    skip_tags = {'tagged'}
    all_vars = {}

    taggable_instance.tags = ['tag1']
    result = taggable_instance.evaluate_tags(only_tags, skip_tags, all_vars)

    assert result is False
