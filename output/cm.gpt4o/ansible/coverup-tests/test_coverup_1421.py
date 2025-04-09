# file lib/ansible/playbook/taggable.py:45-89
# lines [55, 68, 74]
# branches ['54->55', '67->68', '73->74', '82->89', '86->89']

import pytest
from unittest.mock import MagicMock
from ansible.playbook.taggable import Taggable

@pytest.fixture
def taggable():
    taggable = Taggable()
    taggable._loader = MagicMock()
    taggable.tags = ['always', 'test']
    taggable.untagged = set()
    return taggable

def test_evaluate_tags_only_tags_always(taggable, mocker):
    mocker.patch('ansible.playbook.taggable.Templar.template', return_value=['always', 'test'])
    only_tags = {'always'}
    skip_tags = set()
    all_vars = {}

    result = taggable.evaluate_tags(only_tags, skip_tags, all_vars)
    assert result is True

def test_evaluate_tags_only_tags_tagged(taggable, mocker):
    mocker.patch('ansible.playbook.taggable.Templar.template', return_value=['test'])
    only_tags = {'tagged'}
    skip_tags = set()
    all_vars = {}

    result = taggable.evaluate_tags(only_tags, skip_tags, all_vars)
    assert result is True

def test_evaluate_tags_skip_tags_all(taggable, mocker):
    mocker.patch('ansible.playbook.taggable.Templar.template', return_value=['always', 'test'])
    only_tags = set()
    skip_tags = {'all', 'always'}
    all_vars = {}

    result = taggable.evaluate_tags(only_tags, skip_tags, all_vars)
    assert result is False

def test_evaluate_tags_skip_tags_tagged(taggable, mocker):
    mocker.patch('ansible.playbook.taggable.Templar.template', return_value=['test'])
    only_tags = set()
    skip_tags = {'tagged'}
    all_vars = {}

    result = taggable.evaluate_tags(only_tags, skip_tags, all_vars)
    assert result is False
