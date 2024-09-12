# file: lib/ansible/playbook/taggable.py:45-89
# asked: {"lines": [45, 48, 49, 50, 52, 53, 54, 55, 57, 58, 59, 62, 64, 66, 67, 68, 69, 70, 71, 72, 73, 74, 76, 78, 81, 82, 83, 84, 85, 86, 87, 89], "branches": [[48, 49], [48, 62], [53, 54], [53, 58], [54, 55], [54, 57], [66, 67], [66, 78], [67, 68], [67, 69], [69, 70], [69, 71], [71, 72], [71, 73], [73, 74], [73, 76], [78, 81], [78, 89], [81, 82], [81, 84], [82, 83], [82, 89], [84, 85], [84, 86], [86, 87], [86, 89]]}
# gained: {"lines": [45, 48, 49, 50, 52, 53, 54, 57, 58, 59, 62, 64, 66, 67, 68, 69, 71, 72, 73, 76, 78, 81, 84, 85, 86, 89], "branches": [[48, 49], [48, 62], [53, 54], [53, 58], [54, 57], [66, 67], [66, 78], [67, 68], [67, 69], [69, 71], [71, 72], [71, 73], [73, 76], [78, 81], [78, 89], [81, 84], [84, 85], [84, 86], [86, 89]]}

import pytest
from ansible.playbook.taggable import Taggable
from ansible.template import Templar

@pytest.fixture
def taggable_instance(mocker):
    instance = Taggable()
    instance._loader = mocker.Mock()
    instance._loader.get_basedir = mocker.Mock(return_value='.')
    instance.tags = ['test_tag']
    return instance

def test_evaluate_tags_with_only_tags(taggable_instance, mocker):
    mocker.patch.object(Templar, 'template', return_value=['test_tag'])
    only_tags = {'test_tag'}
    skip_tags = set()
    all_vars = {}

    result = taggable_instance.evaluate_tags(only_tags, skip_tags, all_vars)
    assert result is True

def test_evaluate_tags_with_skip_tags(taggable_instance, mocker):
    mocker.patch.object(Templar, 'template', return_value=['test_tag'])
    only_tags = set()
    skip_tags = {'test_tag'}
    all_vars = {}

    result = taggable_instance.evaluate_tags(only_tags, skip_tags, all_vars)
    assert result is False

def test_evaluate_tags_with_both_only_and_skip_tags(taggable_instance, mocker):
    mocker.patch.object(Templar, 'template', return_value=['test_tag'])
    only_tags = {'test_tag'}
    skip_tags = {'skip_tag'}
    all_vars = {}

    result = taggable_instance.evaluate_tags(only_tags, skip_tags, all_vars)
    assert result is True

def test_evaluate_tags_with_untagged(taggable_instance, mocker):
    taggable_instance.tags = None
    only_tags = set()
    skip_tags = set()
    all_vars = {}

    result = taggable_instance.evaluate_tags(only_tags, skip_tags, all_vars)
    assert result is True

def test_evaluate_tags_with_always_tag(taggable_instance, mocker):
    mocker.patch.object(Templar, 'template', return_value=['always'])
    only_tags = {'some_tag'}
    skip_tags = set()
    all_vars = {}

    result = taggable_instance.evaluate_tags(only_tags, skip_tags, all_vars)
    assert result is True

def test_evaluate_tags_with_never_tag(taggable_instance, mocker):
    mocker.patch.object(Templar, 'template', return_value=['never'])
    only_tags = {'some_tag'}
    skip_tags = set()
    all_vars = {}

    result = taggable_instance.evaluate_tags(only_tags, skip_tags, all_vars)
    assert result is False
