# file: lib/ansible/playbook/taggable.py:45-89
# asked: {"lines": [45, 48, 49, 50, 52, 53, 54, 55, 57, 58, 59, 62, 64, 66, 67, 68, 69, 70, 71, 72, 73, 74, 76, 78, 81, 82, 83, 84, 85, 86, 87, 89], "branches": [[48, 49], [48, 62], [53, 54], [53, 58], [54, 55], [54, 57], [66, 67], [66, 78], [67, 68], [67, 69], [69, 70], [69, 71], [71, 72], [71, 73], [73, 74], [73, 76], [78, 81], [78, 89], [81, 82], [81, 84], [82, 83], [82, 89], [84, 85], [84, 86], [86, 87], [86, 89]]}
# gained: {"lines": [45, 48, 49, 50, 52, 53, 54, 57, 58, 59, 62, 64, 66, 67, 69, 70, 71, 72, 78, 81, 82, 83, 84, 85, 86, 87, 89], "branches": [[48, 49], [48, 62], [53, 54], [53, 58], [54, 57], [66, 67], [66, 78], [67, 69], [69, 70], [69, 71], [71, 72], [78, 81], [78, 89], [81, 82], [81, 84], [82, 83], [84, 85], [84, 86], [86, 87]]}

import pytest
from unittest.mock import MagicMock
from ansible.playbook.taggable import Taggable
from ansible.template import Templar

@pytest.fixture
def taggable():
    return Taggable()

def test_evaluate_tags_with_tags(taggable, mocker):
    mocker.patch.object(Templar, 'template', return_value=['tag1', 'tag2'])
    taggable.tags = ['tag1', 'tag2']
    taggable.untagged = set()
    taggable._loader = MagicMock()

    only_tags = ['tag1']
    skip_tags = []
    all_vars = {}

    result = taggable.evaluate_tags(only_tags, skip_tags, all_vars)
    assert result is True

def test_evaluate_tags_with_untagged(taggable):
    taggable.tags = []
    taggable.untagged = set(['untagged'])

    only_tags = []
    skip_tags = []
    all_vars = {}

    result = taggable.evaluate_tags(only_tags, skip_tags, all_vars)
    assert result is True

def test_evaluate_tags_with_only_tags_all(taggable, mocker):
    mocker.patch.object(Templar, 'template', return_value=['tag1'])
    taggable.tags = ['tag1']
    taggable.untagged = set()
    taggable._loader = MagicMock()

    only_tags = ['all']
    skip_tags = []
    all_vars = {}

    result = taggable.evaluate_tags(only_tags, skip_tags, all_vars)
    assert result is True

def test_evaluate_tags_with_skip_tags_all(taggable, mocker):
    mocker.patch.object(Templar, 'template', return_value=['tag1'])
    taggable.tags = ['tag1']
    taggable.untagged = set()
    taggable._loader = MagicMock()

    only_tags = []
    skip_tags = ['all']
    all_vars = {}

    result = taggable.evaluate_tags(only_tags, skip_tags, all_vars)
    assert result is False

def test_evaluate_tags_with_skip_tags(taggable, mocker):
    mocker.patch.object(Templar, 'template', return_value=['tag1'])
    taggable.tags = ['tag1']
    taggable.untagged = set()
    taggable._loader = MagicMock()

    only_tags = []
    skip_tags = ['tag1']
    all_vars = {}

    result = taggable.evaluate_tags(only_tags, skip_tags, all_vars)
    assert result is False

def test_evaluate_tags_with_skip_tags_tagged(taggable, mocker):
    mocker.patch.object(Templar, 'template', return_value=['tag1'])
    taggable.tags = ['tag1']
    taggable.untagged = set(['untagged'])
    taggable._loader = MagicMock()

    only_tags = []
    skip_tags = ['tagged']
    all_vars = {}

    result = taggable.evaluate_tags(only_tags, skip_tags, all_vars)
    assert result is False
