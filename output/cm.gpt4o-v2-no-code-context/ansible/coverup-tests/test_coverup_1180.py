# file: lib/ansible/playbook/taggable.py:45-89
# asked: {"lines": [76], "branches": [[73, 76], [82, 89], [86, 89]]}
# gained: {"lines": [76], "branches": [[73, 76]]}

import pytest
from unittest.mock import MagicMock
from ansible.playbook.taggable import Taggable

@pytest.fixture
def taggable():
    taggable = Taggable()
    taggable.tags = None
    taggable.untagged = set()
    taggable._loader = MagicMock()
    return taggable

def test_evaluate_tags_no_tags(taggable):
    taggable.tags = None
    only_tags = set()
    skip_tags = set()
    all_vars = {}

    result = taggable.evaluate_tags(only_tags, skip_tags, all_vars)
    assert result is True

def test_evaluate_tags_only_tags_false(taggable):
    taggable.tags = ['test']
    only_tags = set(['notest'])
    skip_tags = set()
    all_vars = {}

    result = taggable.evaluate_tags(only_tags, skip_tags, all_vars)
    assert result is False

def test_evaluate_tags_skip_tags_all(taggable):
    taggable.tags = ['test']
    only_tags = set()
    skip_tags = set(['all'])
    all_vars = {}

    result = taggable.evaluate_tags(only_tags, skip_tags, all_vars)
    assert result is False

def test_evaluate_tags_skip_tags_tagged(taggable):
    taggable.tags = ['test']
    only_tags = set()
    skip_tags = set(['tagged'])
    all_vars = {}

    result = taggable.evaluate_tags(only_tags, skip_tags, all_vars)
    assert result is False

def test_evaluate_tags_skip_tags_always(taggable):
    taggable.tags = ['always']
    only_tags = set()
    skip_tags = set(['all', 'always'])
    all_vars = {}

    result = taggable.evaluate_tags(only_tags, skip_tags, all_vars)
    assert result is False
