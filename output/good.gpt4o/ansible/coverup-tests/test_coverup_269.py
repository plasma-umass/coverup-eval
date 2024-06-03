# file lib/ansible/playbook/taggable.py:33-43
# lines [33, 34, 35, 36, 37, 38, 39, 41, 43]
# branches ['34->35', '34->36', '36->37', '36->43', '38->39', '38->41']

import pytest
from ansible.errors import AnsibleError
from ansible.playbook.taggable import Taggable

@pytest.fixture
def taggable():
    return Taggable()

def test_load_tags_list(taggable):
    ds = ['tag1', 'tag2']
    result = taggable._load_tags('attr', ds)
    assert result == ds

def test_load_tags_string(taggable):
    ds = 'tag1, tag2, tag3'
    result = taggable._load_tags('attr', ds)
    assert result == ['tag1', 'tag2', 'tag3']

def test_load_tags_invalid_type(taggable):
    ds = 123
    with pytest.raises(AnsibleError, match='tags must be specified as a list'):
        taggable._load_tags('attr', ds)
