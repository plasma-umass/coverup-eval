# file: lib/ansible/playbook/taggable.py:45-89
# asked: {"lines": [45, 48, 49, 50, 52, 53, 54, 55, 57, 58, 59, 62, 64, 66, 67, 68, 69, 70, 71, 72, 73, 74, 76, 78, 81, 82, 83, 84, 85, 86, 87, 89], "branches": [[48, 49], [48, 62], [53, 54], [53, 58], [54, 55], [54, 57], [66, 67], [66, 78], [67, 68], [67, 69], [69, 70], [69, 71], [71, 72], [71, 73], [73, 74], [73, 76], [78, 81], [78, 89], [81, 82], [81, 84], [82, 83], [82, 89], [84, 85], [84, 86], [86, 87], [86, 89]]}
# gained: {"lines": [45, 48, 49, 50, 52, 53, 54, 57, 58, 59, 62, 64, 66, 67, 69, 71, 72, 73, 76, 78, 81, 84, 85, 86, 89], "branches": [[48, 49], [48, 62], [53, 54], [53, 58], [54, 57], [66, 67], [66, 78], [67, 69], [69, 71], [71, 72], [71, 73], [73, 76], [78, 81], [78, 89], [81, 84], [84, 85], [84, 86], [86, 89]]}

import pytest
from ansible.playbook.taggable import Taggable
from ansible.template import Templar

class MockLoader:
    def get_basedir(self):
        return './'

@pytest.fixture
def taggable():
    class TestTaggable(Taggable):
        def __init__(self):
            self.tags = []
            self._loader = MockLoader()
    return TestTaggable()

@pytest.fixture
def templar():
    return Templar(loader=MockLoader(), variables={})

def test_evaluate_tags_no_tags(taggable):
    assert taggable.evaluate_tags(only_tags=None, skip_tags=None, all_vars={}) == True

def test_evaluate_tags_with_tags(taggable, monkeypatch):
    taggable.tags = ['test']
    monkeypatch.setattr(Templar, 'template', lambda self, var: var)
    assert taggable.evaluate_tags(only_tags=None, skip_tags=None, all_vars={}) == True

def test_evaluate_tags_only_tags(taggable, monkeypatch):
    taggable.tags = ['test']
    monkeypatch.setattr(Templar, 'template', lambda self, var: var)
    assert taggable.evaluate_tags(only_tags=['test'], skip_tags=None, all_vars={}) == True
    assert taggable.evaluate_tags(only_tags=['notest'], skip_tags=None, all_vars={}) == False

def test_evaluate_tags_skip_tags(taggable, monkeypatch):
    taggable.tags = ['test']
    monkeypatch.setattr(Templar, 'template', lambda self, var: var)
    assert taggable.evaluate_tags(only_tags=None, skip_tags=['test'], all_vars={}) == False
    assert taggable.evaluate_tags(only_tags=None, skip_tags=['notest'], all_vars={}) == True

def test_evaluate_tags_only_and_skip_tags(taggable, monkeypatch):
    taggable.tags = ['test']
    monkeypatch.setattr(Templar, 'template', lambda self, var: var)
    assert taggable.evaluate_tags(only_tags=['test'], skip_tags=['test'], all_vars={}) == False
    assert taggable.evaluate_tags(only_tags=['test'], skip_tags=['notest'], all_vars={}) == True
